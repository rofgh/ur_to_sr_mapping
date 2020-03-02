import re
import numpy as np
from sys import exit
from matplotlib.pyplot import plot, show, legend, title, xlabel, ylabel, ylim, xlim
from random import shuffle, choice

##SETTINGS SET BY USER###################################################
#Name of the training data file:
TRAINING_FILE = "VerbHead+VMov_Strong+VMov_Weak+Topic+Uber_EPP+EPP_Type - Training Data.txt" 
EPOCHS = 10 #i.e. how many full passes through the data you make (learning is online!)
LEARNING_RATE = 0.1  #i.e. how much you weight each new estimated grammar (0-1)
SAMPLE_NUM = 25 #how many samples you take to estimate Pr(data|grammar)
REPS = 5 #How many times you'll run each language
RAND_INIT = False #If false, initial parameter probs=.5

#A list of labels for each parameter in the same order 
#that they're given in the training file:
PARAM_LIST = ["VerbHead", "VMov_Strong", "VMov_Weak", "Topic", "Uber_EPP", "EPP_Type"] 

#What language do you want to plot the parameter values for? 
#If this is "", plot overall learning curves instead.
PLOT_PARAMS_FOR = "" 
#########################################################################

##PROCESS TRAINING FILE##################################################
td_file = open(TRAINING_FILE)
all_mappings = {}
all_languages = []
failures = []
for line in td_file.readlines():
    line = line.rstrip()
    if len(line) == 0:
        exit("Remove all blank lines from training data file!")
    if line[0] == "*": #New Language
        continue
    elif line[0] == "-": #Start reading the data
        continue
    elif re.search("\d", line): #Language Label/Param settings
        language = line
        all_languages.append(language)
        all_mappings[language] = {}
    elif re.search("[a-zA-Z]", line): #Input/Output pair
        meaning, surface_string = line.split("\t")
        all_mappings[language][meaning] = surface_string
    else:
        exit("Training File Error!!")
td_file.close()
#########################################################################

#TEST FUNCTION#################################################
def testModel (param_probs, test_data):
    #This function returns an estimate of the probability of test_data given param_probs.
    testing_successes = []
    for s in range(SAMPLE_NUM):
        this_sample = np.random.rand(param_probs.shape[0]) < param_probs #Array of random parameter settings.
        sample_setting = "".join([str(int(s)) for s in this_sample])
        test_success = 1.0
        for d in test_data:
            if all_mappings[sample_setting][d[0]] == d[1]:
                continue
            else:
                test_success = 0.0
                break
        testing_successes.append(test_success)
    return np.mean(testing_successes)

def percCorr (param_probs, test_data):
    #This function returns the percent correct across all the data on a single sample of the grammar.
    testing_successes = []
    for d in test_data:
        this_sample = np.random.rand(param_probs.shape[0]) < param_probs #Array of random parameter settings.
        sample_setting = "".join([str(int(s)) for s in this_sample])
        if all_mappings[sample_setting][d[0]] == d[1]:
            testing_successes.append(1.0)
        else:
            testing_successes.append(0.0)
    return np.mean(testing_successes)    
#########################################################################

#LEARN FOR EACH LANGUAGE#################################################
learning_curves = {l:[[] for rep in range(REPS)] for l in all_languages}
first_updates = {l:{} for l in all_languages}
param_curves = {r:[] for r in range(REPS)}
rounded2exact = {}
for rep in range(REPS):
    for lang in all_languages:
        #Set initial parameter probabilities:
        if RAND_INIT:
            param_probs = np.random.uniform(low=0.0, high=1.0, size=len(PARAM_LIST))
            init = str(param_probs[:])
        else:
            init = "Non-Random (.5)"
            param_probs = np.array([.5 for p in PARAM_LIST])
		
			
        if lang == PLOT_PARAMS_FOR:
            for param_val in param_probs:
                param_curves[rep].append([param_val])
				
        
        #Construct training data for this language:
        training_data = []
        for IN in all_mappings[lang].keys():
            training_data.append((IN,all_mappings[lang][IN]))  
        #Go through all the data each epoch:
        for epoch in range(EPOCHS): 
            shuffle(training_data)         
            for datum in training_data:
                IN = datum[0] #Input (i.e. meaning)
                OUT = datum[1] #Output (i.e. flattened surface string)
                new_grammar = np.zeros_like(param_probs) #Empty array to hold new, estimated grammar
                
                #Loop through each parameter, seeing what happens when it's held in the on/off positions:
                for main_param, main_prob in enumerate(param_probs):
                    freqGivenOn = 0.0
                    freqGivenOff = 0.0
                    
                    #Sample the values of the other parameters:
                    for s in range(SAMPLE_NUM):
			#Array of random parameter settings:
                        this_sample = np.random.rand(param_probs.shape[0]) < param_probs 
                        sample_settings_ON = "" #Settings if main_param is on
                        sample_settings_OFF = "" #Settings if main_param is off
                        
                        #Loop through each parameter, adding its value to the relevant strings:
                        for param, onOrOff in enumerate(this_sample):
                            if param == main_param:
                                sample_settings_ON += "1"
                                sample_settings_OFF += "0"
                            else:
                                sample_settings_ON += str(int(onOrOff))
                                sample_settings_OFF += str(int(onOrOff))
                        
                        #Check to see if the predicted outputs match the correct output:
                        if all_mappings[sample_settings_ON][IN] == OUT:
                            freqGivenOn += 1.0
                        if all_mappings[sample_settings_OFF][IN] == OUT:
                            freqGivenOff += 1.0
                    
                    #Use the sample drawn above to calculate the necessary probs:    
                    probGivenOn = (freqGivenOn/SAMPLE_NUM) + .0001
                    probGivenOff = (freqGivenOff/SAMPLE_NUM) + .0001
                    probDatumGivenGrammar = (probGivenOn * param_probs[main_param]) + \
                                            (probGivenOff * (1.0 - param_probs[main_param]))\
                                            + .0001
                    prob_on = (probGivenOn * param_probs[main_param])/probDatumGivenGrammar
                    
                    #Store this estimate of the paramter's ON probability:
                    new_grammar[main_param] = prob_on
                
                #Update, weighting the new grammar according to the learning rate:
                param_probs = (new_grammar*LEARNING_RATE) + (param_probs*(1-LEARNING_RATE))
                
                #Save the first update we make to each parameter for each datum:
                if epoch == 0:
                    first_updates[lang][datum] = new_grammar
                    
                #Save the parameter values if this is the right lang:
                if lang == PLOT_PARAMS_FOR:
                    for param_index, param_val in enumerate(param_probs):
                        param_curves[rep][param_index].append(param_val)
						
                
            performance = testModel(param_probs, training_data)
            learning_curves[lang][rep].append(performance)
         
	#Keep track of failures:
        #if performance < .9: #learning criterion is pr(data|grammar)>=.9
            #failures.append([init, performance, learning_curves[lang][rep]])
			
        #Print learned parameter probabilities:
        #learned_params = ",".join([str(pps) for pps in param_probs])
        #rounded_params = "".join([str(int(round(pps, 0))) for pps in param_probs])
        #print lang+": "+rounded_params+" (Rep="+str(rep)+")"+" Learned? "+str(rounded_params==lang)
        #if rounded_params!=lang and lang[1] == "0" and lang[4]=="0":
            #exit(init)
                
######################################################################### 

##OUTPUT##################################################
if PLOT_PARAMS_FOR == "":
#Plot learning curves for all languages:
    for lang in learning_curves.keys():
        mean_curve = np.mean(learning_curves[lang], axis=0)
        plot(range(len(mean_curve)), mean_curve, label=lang, linestyle=choice(["--", "-"]), marker="$"+lang+"$", markersize=20, markevery=choice([1, 2]))
    l = legend()
    l.draggable()
    title("Learning Curves (all languages)")
    xlabel("Epoch")
    ylabel("Pr(Full Dataset|Grammar)")
    #xlim(0,EPOCHS)
    ylim(0, 1)
else:
#Plot learning curves for a single language's parameters: 
    by_param = {p:[] for p in range(len(PARAM_LIST))}
    for rep in param_curves.keys():
        for param_num, param_curve in enumerate(param_curves[rep]):
            by_param[param_num].append(param_curve)

    for param_num in by_param.keys():
        curve = np.mean(by_param[param_num], axis=0)
        plot(curve, label=str(PARAM_LIST[param_num]))
        l = legend()
        l.draggable()  
        title("Parameter Learning Curves for "+PLOT_PARAMS_FOR)
        xlabel("Update (one per datum, per epoch)")
        ylabel("Pr(Parameter=1)")
        ylim(0,1)  
show()
######################################################################### 

#Save to a csv file:
save_file = open("performance_curve_EDL.csv", "w")
save_file.write("Language,Repetition,"+",".join(["Epoch_"+str(e) for e in range(EPOCHS)])+"\n")
for lang in learning_curves.keys():
	for rep, curve in enumerate(learning_curves[lang]):
		save_file.write('_'+lang+'_'+","+str(rep)+","+",".join([str(x) for x in curve])+"\n")
		
save_file.close()     



