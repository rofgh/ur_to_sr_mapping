'''
SR creator
takes the UR list, at all_URs.txt, for each one of them it runs the obj-maker, at obj-maker.py
producing, hopefully, a list of SRs/SOWs
'''

#from modules    import *

from modules.nodes      import nodes
from modules.parameters import apply_parameters
from modules.URs        import all_URs
import sys


# generates all the language possibilities
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
# Requires pre-running of URs.py, if not already run
def activate_force(force):
    filename = "UR_writer/all_"+force+"URs.txt"
    with open(filename, 'r') as u:
        URs = u
        all_URs = []
        for UR in URs.readlines():
            all_URs.append(UR)
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
    all_forces      = ["I"]
    for x in all_forces:
        yield x


if __name__ == '__main__':
    try:
        all = bool(sys.argv[1])
    except: 
        all = False
    all_URs()
    treecount = 0
    filename = "all_all.txt"
    with open(filename, 'w') as f:
        for language in languages(all):
            for force in forces():
                all_URs = activate_force(force)
                for ur in all_URs:
                    node = nodes(ur)
                    node = apply_parameters(language, force, node)
                    if node != "Not parseable!":
                        #SR = produce(language, force, ur, nodes)
                        treecount += 1
                        pass
                    else:
                        SR = node
                    for dig in language:
                        f.write(str(dig)+"")
                    f.write("\t"+force+"\t")
                    f.write(ur)
                    #f.write(ur+"\t")
                    #f.write(SR)
    print("assessed "+str(treecount)+" trees and wrote them to "+filename)
