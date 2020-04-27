import csv

# generates the language possibilities
def languages(all=False):
    # FOR ALL LANGUAGES
    if all == True:
        for x in range(0, 8192):
            language = []
            for digit in format(x, '013b'):
                if digit == '0':
                    language.append(0)
                if digit == '1':
                    language.append(1)
            yield language
    ### ENGLISH ONLY: (Or add other specific languages)
    if all == False:
        english = [ 
        [0,0,0,0,0,0,0,0,1,0,0,0,0],    #Topic Marking
        [0,0,0,1,0,0,1,1,0,0,0,1,1],    #English
        [0,0,0,0,0,0,0,0,0,0,0,0,0],    #All off
        [0,0,0,0,0,0,0,0,0,0,0,0,1],    #All off, but obl Q inversion
        [1,0,0,0,0,0,0,0,0,0,0,0,0],    #All off, but Left Subject pos
        [1,1,1,1,1,1,1,1,1,1,1,1,1],    #All on
        [0,0,0,1,1,1,0,0,1,0,0,0,0],    #OptTop, Null Top, Null Sub, Topic Marking
        [1,1,1,1,0,0,0,0,0,0,0,1,0]     #All Right Head, OptTop, Affix Hopping
        ]    
        for x in english:
            yield x

# selects a illocutionary force and produces all the possible URs for that force
# Requires pre-running of URs.py, if not already run in this script (currently line 68)


###  PAD LIST WITH 14, instead of what is happening here
def activate_force(force):
    filename = "src/UR_writer/all_"+force+"URs.txt"
    with open(filename, 'r') as u:
        URs = u
        all_URs = []
        for UR in URs.readlines():
            UR = UR.split()
            full_UR = ['\t']*14
            for x in range(len(UR)):
                full_UR[x] = UR[x]
            all_URs.append(full_UR)
            #print(len(full_UR))
    return all_URs

# just a test
def assert_length(doc):
    with open(doc, "r") as r:
        for i, l in enumerate(r):
                pass
    assert i+1 == (len(all_forces)*len(current_langs)*len(all_URs))

#mostly just playing with yield, but a generator for the forces
def force_finder(forces):
    if forces == True:
        all_forces      = ["D","I","Q"]
    else:
        all_forces      = ["D"]
    for x in all_forces:
        yield x

def realize(node, string):
    string += node.name+"\t"
    return string

def expand(node, string):
    lis = node.daughters
    lis_names = []
    for x in lis:
        lis_names.append(x.name)
    #assert len(lis) < 4, str(node.name)+" has too many daughters: "+str(len(lis))+": "+str(lis_names)
    '''
    for x in lis:
        print(x, end=",")
    '''
    if len(lis) == 0:
        if node.null == False:
            string = realize(node, string)
    if len(lis) != 0:
        for x in lis:
            if x.pos == "L":
                string = expand(x, string)
        for x in lis:
            if x.pos == None:
                string = expand(x, string)
        for x in lis:
            if x.pos == "R":
                string = expand(x, string)
    return string

# out gets called for each SOW
def out(language, force, ur, nodes):
    if len(nodes)>24 and isinstance(nodes, list):
        print("why are there "+str(len(nodes))+" nodes in this list...")
        return
    with open('all_all.tsv', 'a') as f:
        output = csv.writer(f, delimiter='\t')
        #initializes row
        row = []  
        #row[0]=language
        digits = ''
        for dig in language:
            digits += str(dig)
        row.append(digits)
        # row[1]=force
        row.append(force)
        # Writes out the UR
        #row[2:16]=ur
        for item in ur:
            row.append(item)
        #row[16]="SR:"
        row.append("SR:")
        #After this the SR items are produced
        #If SR is unparseable, a not parseable message is produced
        if isinstance(nodes, str):
            row.append(nodes)
        #Else, start in the CP node and work down the tree
        if isinstance(nodes, list):
            for n in nodes:
                if n.name != "CP":
                    pass
                if n.name == "CP":
                    string = ''
                    row.append(expand(n, string))
        row.append('\n')
        output.writerow(row)
    return
        
def get_daughters(UR):
    if "Not parseable" not in UR:
        assert len(UR) == 22
        for n in UR:
            if n.mother:
                n.mother.daughters.append(n)
    return UR