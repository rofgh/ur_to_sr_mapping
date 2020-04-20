

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
        english = [[0,0,0,1,0,0,1,1,0,0,0,1,1]]
        for x in english:
            yield x

# selects a illocutionary force and produces all the possible URs for that force
# Requires pre-running of URs.py, if not already run in this script (currently line 68)


###  PAD LIST WITH 14, instead of what is happening here
def activate_force(force):
    filename = "modules/UR_writer/all_"+force+"URs.txt"
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
def forces():
    #all_forces      = ["D","I","Q"]
    all_forces      = ["D"]
    for x in all_forces:
        yield x

def realize(node, string):
    string += node.name+"\t"
    return string

def expand(node, string):
    if node.real == True and node.inUR == True and node.null == False:
        string = realize(node, string)
    lis = node.daughters
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
    with open("all_all.txt", 'a') as f:
        # writes out the language
        for dig in language:
            f.write(str(dig)+"")
        # Writes out the force
        f.write("\t"+force+"\t")
        # Writes out the UR
        for item in ur:
            if item != "\t":
                f.write(item+"\t")
            else:
                f.write(item)
        f.write("SR:\t")
        if nodes == "Not parseable!":
            f.write(nodes+"\n")
        else:
            assert isinstance(nodes, list), type(nodes)
            for n in nodes:
                if n.name != "CP":
                    pass
                if n.name == "CP":
                    string = ''
                    f.write(expand(n, string))
        f.write("\n")
    return
        
def get_daughters(UR):
    for x in UR:
        if x.mother:
            y = x.mother
            y.daughters.append(x)
        else:
            pass
    return UR