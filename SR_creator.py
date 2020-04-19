'''
SR creator
takes the UR list, at all_URs.txt, for each one of them it runs the obj-maker, at obj-maker.py
producing, hopefully, a list of SRs/SOWs
'''

#from modules    import *

from modules.nodes      import nodes
from modules.parameters import apply_parameters
from modules.URs        import all_URs
from modules            import test_parse
import sys


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


if __name__ == '__main__':
    open("all_all.txt", 'w')
    try:
        arg = sys.argv[1]
        if arg == 'True':
            all = True
        else:
            all = False
    except:
        all = False
    # runs the UR_writing script, creating .txt files for each force
    all_URs()
    tree_count = 0
    for language in languages(all):
        # runs through the list of forces
        for force in forces():
            # returns list of lists, padded to 14 items (i.e. the most lexical items possible)
            all_URs = activate_force(force)
            # for each UR in this force's list of URs
            for ur in all_URs:
                # Take the UR, turn it into list of node objects
                node_list = nodes(ur)
                # Run each UR through the parameter settings;
                # Each UR (and its nodes/tree) can produce multiple SR/strings
                # so l_of_l_of_nodes can be max 6 lists of nodes
                # based on optional parameter settings: (null_subXnull_topXprep_stranding) = 6
                PFN             = [[]]*3
                PFN[0]          = language
                PFN[1]          = force
                PFN[2]          = node_list
                l_of_l_of_nodes = apply_parameters(PFN)
                assert len(l_of_l_of_nodes)>0
                # Finally make the SOWs/SRs
                for l_of_nodes in l_of_l_of_nodes:
                    if len(l_of_nodes)>0:
                        tree_count += 1
                        # Make an SOW/SR for each node list
                        # i.e. for each possible outcome of parameters & ur
                        out(language, force, ur, l_of_nodes)
            

    print("assessed "+str(tree_count)+" trees and wrote them to "+"all_all.txt")
    test_parse
