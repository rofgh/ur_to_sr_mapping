from itertools import product
import re
from sys import exit

####Build a list of different languages:
params = ["VerbHead", "VMov_Strong", "VMov_Weak", "Topic", "Uber_EPP", "EPP_Type"]
languages = ["".join(l) for l in product(["0", "1"], repeat=len(params))]

####Build a list of different underlying sentences:
#Words:
words = [    
            "[c]", #Empty C
            "[Pc]", #C with phonological content
            "[l]", #Landing site for verbs and aux, aka [T]
            "[A]", #Adverb
            "[At]", #Topicalized adverb
            "[U]", #Aux
            "[S]", #Subject
            "[St]", #Topicalized subject
            "[V]", #Verb
            "[O]", #Object
            "[Ot]", #Topicalized object
        ]

#Basic meanings:
meanings = [
                #Empty C
                "[c][l][St][V]",
                "[c][l][St][V][O]",
                "[c][l][S][V][Ot]",
                "[c][l][U][St][V]",
                "[c][l][U][St][V][O]",
                "[c][l][U][S][V][Ot]",
                "[c][l][A][St][V]",
                "[c][l][At][S][V]",
                "[c][l][A][St][V][O]",
                "[c][l][At][S][V][O]",
                "[c][l][A][S][V][Ot]",
                "[c][l][U][A][St][V]",
                "[c][l][U][At][S][V]",
                "[c][l][U][A][St][V][O]",
                "[c][l][U][A][S][V][Ot]",
                "[c][l][U][At][S][V][O]",
                
                #Contentful C
                "[Pc][l][St][V]",
                "[Pc][l][St][V][O]",
                "[Pc][l][S][V][Ot]",
                "[Pc][l][U][St][V]",
                "[Pc][l][U][St][V][O]",
                "[Pc][l][U][S][V][Ot]",
                "[Pc][l][A][St][V]",
                "[Pc][l][At][S][V]",
                "[Pc][l][A][St][V][O]",
                "[Pc][l][At][S][V][O]",
                "[Pc][l][A][S][V][Ot]",
                "[Pc][l][U][A][St][V]",
                "[Pc][l][U][At][S][V]",
                "[Pc][l][U][A][St][V][O]",
                "[Pc][l][U][A][S][V][Ot]",
                "[Pc][l][U][At][S][V][O]",

            ]

####Handcode parameters:
def VerbHead (IN, params):
    OUT = IN        
    if params[0] == "0":
        #V to the right of O,
        if "O" in IN:
            OUT = re.sub(re.escape("[V]"),"", OUT)
            OUT = re.sub(re.escape("[O]"), "[O][V]", OUT)
            OUT = re.sub(re.escape("[Ot]"), "[Ot][V]", OUT)
        #U to the right of V
        if "U" in IN:
            OUT = re.sub(re.escape("[U]"),"", OUT)
            OUT = re.sub(re.escape("[V]"), "[V][U]", OUT)
        if "l" in IN:
            OUT = re.sub(re.escape("[l]"),"", OUT)
            if "U" in OUT:
                OUT = re.sub(re.escape("[U]"), "[U][l]", OUT)
            else:
                OUT = re.sub(re.escape("[V]"), "[V][l]", OUT)
    if params[0] == "1":
        #V to the left of O,
        if "O" in IN:
            OUT = re.sub(re.escape("[V]"),"", OUT)
            OUT = re.sub(re.escape("[O]"), "[V][O]", OUT)
            OUT = re.sub(re.escape("[Ot]"), "[V][Ot]", OUT)
        
    return OUT

def VMov_Strong (IN, params):
    OUT = IN
    if params[1] == "0":
        return OUT
    elif "U" not in OUT:
        OUT = re.sub(re.escape("[V]"), "", OUT)
        OUT = re.sub(re.escape("c]"), "c][V]", OUT)
    else:
        OUT = re.sub(re.escape("[U]"), "", OUT)
        OUT = re.sub(re.escape("c]"), "c][U]", OUT)
    return OUT+"%"
    

def VMov_Weak (IN, params):
    OUT = IN
    if params[2] == "0":
        return OUT
    elif "Pc" in OUT:
        return OUT
    elif "U" not in OUT:
        OUT = re.sub(re.escape("[V]"), "", OUT)
        OUT = re.sub(re.escape("c]"), "c][V]", OUT)
    else:
        OUT = re.sub(re.escape("[U]"), "", OUT)
        OUT = re.sub(re.escape("c]"), "c][U]", OUT)
    return OUT+"%"

def Uber_EPP (IN, params):
    OUT = IN
    if params[4]=="0":
        return OUT+"$"
    elif params[4]=="1":
        #First EPP type:
        if params[0] == "0":
            if "A" in OUT:
                if "[St]" in OUT:
                    OUT = re.sub(re.escape("[St]"), "", OUT)
                    OUT = re.sub(re.escape("[A]"), "[St][A]", OUT)
                    OUT = re.sub(re.escape("[At]"), "[St][At]", OUT)
                else:
                    OUT = re.sub(re.escape("[S]"), "", OUT)
                    OUT = re.sub(re.escape("[A]"), "[S][A]", OUT)
                    OUT = re.sub(re.escape("[At]"), "[S][At]", OUT)
        elif params[0] == "1":
            if "[St]" in OUT:
                OUT = re.sub(re.escape("[St]"), "", OUT)
                OUT = re.sub(re.escape("[l]"), "[St][l]", OUT)
            else:
                OUT = re.sub(re.escape("[S]"), "", OUT)
                OUT = re.sub(re.escape("[l]"), "[S][l]", OUT)
                
        #Second EPP type:
        if "[U]" in OUT:
            OUT = re.sub(re.escape("[U]"), "", OUT)
            OUT = re.sub(re.escape("[l]"), "[U]", OUT)
        else:
            OUT = re.sub(re.escape("[V]"), "", OUT)
            OUT = re.sub(re.escape("[l]"), "[V]", OUT)
          
    return OUT

def EPP_Type (IN, params):
    if "$" not in IN:
        return IN
    else:
        OUT = re.sub("\$", "", IN)
        if params[5] == "0":
            #First type:
            #Headedness matters! (in head=0, s goes to left of A
            if params[0] == "0":
                if "A" in OUT:
                    if "[St]" in OUT:
                        OUT = re.sub(re.escape("[St]"), "", OUT)
                        OUT = re.sub(re.escape("[A]"), "[St][A]", OUT)
                        OUT = re.sub(re.escape("[At]"), "[St][At]", OUT)
                    else:
                        OUT = re.sub(re.escape("[S]"), "", OUT)
                        OUT = re.sub(re.escape("[A]"), "[S][A]", OUT)
                        OUT = re.sub(re.escape("[At]"), "[S][At]", OUT)
            elif params[0] == "1":
                if "[St]" in OUT:
                    OUT = re.sub(re.escape("[St]"), "", OUT)
                    OUT = re.sub(re.escape("[l]"), "[St][l]", OUT)
                else:
                    OUT = re.sub(re.escape("[S]"), "", OUT)
                    OUT = re.sub(re.escape("[l]"), "[S][l]", OUT)
        elif params[5] == "1":
            #Second type:
            if "[U]" in OUT:
                OUT = re.sub(re.escape("[U]"), "", OUT)
                OUT = re.sub(re.escape("[l]"), "[U]", OUT)
            else:
                OUT = re.sub(re.escape("[V]"), "", OUT)
                OUT = re.sub(re.escape("[l]"), "[V]", OUT) 
    return OUT     
            
def Topic (IN, params):
    if "%" not in IN:
        return IN
    else:
        IN = re.sub("%", "", IN)
    if params[3] == "1":
        words = IN.split("][")
        topic_index = -1
        for i, word in enumerate(words):
            if "t" in word:
                topic_index = i
                break
        if topic_index == -1:
            return IN
        topped_word = words[topic_index]
        words.remove(topped_word)
        topped_word = re.sub("\]", "", topped_word)
        words = [words[0], topped_word]+words[1:]
        OUT = "][".join(words)
        if OUT[-1] != "]":
            OUT += "]"
        return OUT
    else:
        return IN
        
####Write the actual data file:
WD = "C:\\Users\\Brandon\\OneDrive\\Research\\Hidden Structure\\Syntax\\6 Parameter Training Data\\"
output_file = open(WD+"+".join(params)+" - Training Data.txt", "w")
for lang in languages:
    output_file.write("*******************************\n")
    output_file.write(lang+"\n")
    output_file.write("------------------------------\n")
    for meaning in meanings:   
        output_file.write(meaning+"\t")
        my_sent = meaning
        
        #Apply functions here:
        print "Meaning: ", my_sent
        my_sent = VerbHead(my_sent, lang)
        print "After VerbHead: ", my_sent
        
        #if lang[0] == "1" and "U" in my_sent:
        #    if "St" in my_sent:
        #        my_sent = re.sub(re.escape("[St]"), "", my_sent)
        #        my_sent = re.sub(re.escape("[U]"), "[St][U]", my_sent)
        #    else:
        #        my_sent = re.sub(re.escape("[S]"), "", my_sent)
        #        my_sent = re.sub(re.escape("[U]"), "[S][U]", my_sent)
        #if lang[0] == "0" and "U" in my_sent and "A" in my_sent:
        #    if "St" in my_sent:
        #        my_sent = re.sub(re.escape("[St]"), "", my_sent)
        #        my_sent = re.sub(re.escape("[At]"), "[St][At]", my_sent)
        #        my_sent = re.sub(re.escape("[A]"), "[St][A]", my_sent)
        #    else:
        #        my_sent = re.sub(re.escape("[S]"), "", my_sent)
        #        my_sent = re.sub(re.escape("[A]"), "[S][A]", my_sent)
        #        my_sent = re.sub(re.escape("[At]"), "[S][At]", my_sent)
        
        my_sent = Uber_EPP(my_sent, lang)
        print "After Uber EPP: ", my_sent
        my_sent = EPP_Type(my_sent, lang)
        print "After EPP type: ", my_sent 
        my_sent = VMov_Strong(my_sent, lang)
        print "After Strong Move: ", my_sent
        my_sent = VMov_Weak(my_sent, lang)
        print "After Weak Move: ", my_sent     
        my_sent = Topic(my_sent, lang)
        print "After Topic: ", my_sent

        
        #if meaning == "[c][l][St][V]" and lang == "000000":
            #exit()
            
        #Clean up the output so that only surface structure is visible:
        my_sent = re.sub("\[[a-z]+\]", "", my_sent)
        my_sent = re.sub("[a-z]", "", my_sent)
        
        #Write to file:
        output_file.write(my_sent+"\n")
output_file.close()
        


