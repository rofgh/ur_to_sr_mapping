'''
Current problem:
Currently able to run one sentence for each language setting,
but how to run all the different URs within each language??
Parameter functions turn on or off everything, and then the next step is to step through each possible 
UR within that?
-->>  process_parameters produces all the URs for a language?


#5:
For VtoI movement, at the moment the mechanism requires the daughters to be set up, so the get_daughters
function will have to have been run

#6:
TOPIC   = Topic Node
    TOPIC.mother = CP
if '[+WH]' in node.name:
    new = node.name
    node.name = new.remove('[+WH]')
    WH      = node
    node.daughter += Wh

These both need to point to the same node if they are the same....
'''
def produce():
    return
    
#initialize the illocutionary force, which (dis)allows certain nodes and movement?
# Q: Wh becomes realized and non-null
# DEC: ???
# IMP: Imperatives are immune to all parametric variation except headedness
def illoc_force_setup(UR, illoc):
    for x in UR:
        if x.name == "[+WH]" and illoc == "Q":
            x.null = False
        if x.name == " S" and illoc == "D":
            x.null = False  
        if x.name == " V" and illoc == "D":
            x.null = False
        if x.name == " V" and illoc == "I":
            x.null = False
    return UR
    pass

def noparse():
    output = "Not parseable"
    output(output)

def output(x):
    #print to terminal
    print(x)
    #print to output file:
    with open(out_filename, 'w') as f:
        f.write(x)
        
#######EXPAND: jumps through the nodes and realizes them if they are realizable
# then opens their daughters, if there are any (meaning that if you are a realizable node with daughters
# you get realized then expand)

def expand(node):
    if node.real == True and node.inUR == True and node.null == False:
        realize(node)
    lis = node.daughters
    if len(lis) != 0:
        for x in lis:
            if x.pos == "L":
                expand(x)
        for x in lis:
            if x.pos == None:
                expand(x)
        for x in lis:
            if x.pos == "R":
                expand(x)

#######REALIZE: if a realizable node is reached, it's x.name is printed
def realize(node):
        print(node.name, end = '')
        return


if __name__ == '__main__':
    ### ALL THE PARAMETER SETTINGS ####
    for x in range(0, 8192):
        language = []
        for digit in format(x, '013b'):
            if digit == '0':
                language.append(0)
            if digit == '1':
                language.append(1)
        print("Language "+str(x+1)+": "+str(language))
        UR = produce_UR()
        illocs = ["Q", "D", "I"]
        UR_list = []
        for x in illocs:

            base_UR = illoc_force_setup(UR, x)
            base_UR = process_parameters(language, base_UR)
            #UR_list = UR_permutations(base_UR)
            for x in UR:
                if x.null == False:
                    print(x.name, end="")
            print()
        '''
        for UR in all_lang_URs:    
            # is each UR an.... object of its own?
            expand(CP)
            print()
            print()
        '''
