import csv
from .ind_variables import * 
from .URs import *

# selects a illocutionary force and produces all the possible URs for that force
# Requires pre-running of URs.py, if not already run in this script (currently line 68)
###  PAD LIST WITH 14, instead of what is happening here??
def activate_force(force, UR_file):
    #for all forces and all URS
    if UR_file == True:
        URs = new_all_URs(force)
    #If user defined URs are in play
    else:
        URs = limited_UR_list()
    return URs

# just a check function, it should now be obsolete
def assert_length(doc):
    with open(doc, "r") as r:
        for i, l in enumerate(r):
                pass
    assert i+1 == (len(all_forces)*len(current_langs)*len(all_URs))

#Very important function, expands each node according to its headedness!
def expand(node, row):
    '''
    if len(daught)>0:
        print(node.name, end=": ")
        for x in daught:
            print(x.name, end=',')
        print()
    '''
    if node.null == False:
        row = realize(node, row)
        #print(node.name)
    if len(node.daughters) != 0:
        for x in node.daughters:
            if x.pos == "L":
                row = expand(x, row)
        for x in node.daughters:
            if x.pos == None:
                row = expand(x, row)
        for x in node.daughters:
            if x.pos == "R":
                row = expand(x, row)
    return row

#mostly just playing with yield, but a generator for the forces
def force_finder(forces):
    if forces == True:
        selected_forces      = ["D","I","Q"]
    else:
        selected_forces      = limited_forces_list()
    for x in selected_forces:
        yield x

#Produces daughters from all node.mothers, but must happen after all movement       
def get_daughters(UR):
    if "Not parseable" not in UR:
        assert len(UR) == 22
        for n in UR:
            if n.mother:
                if isinstance(n.mother, str):
                    print(n.mother)
                n.mother.daughters.append(n)
                if n.name == '[+wa]':
                    #print("[+wa]'s mother: ", end='')
                    #print(n.mother.name, end=' is null: ')
                    #print(n.mother.null)
                    pass
            if n.null == False:
                #print(n.name, end=' ')
                pass
    return UR

# generates the 8192 parameter setting possibilities, or returns the user-modified list
def languages(all=False):
    # FOR ALL LANGUAGE FAMILIES (i.e. every permutation of parameters)
    if all == True:
        for x in range(0, 8192):
            language = []
            for digit in format(x, '013b'):
                if digit == '0':
                    language.append(0)
                if digit == '1':
                    language.append(1)
            yield language
    ### SEE INDEPENDENT VARIABLES LIST
    if all == False:
        limited_languages = limited_languages_list()
        for x in limited_languages:
            yield x

# out gets called for each SOW, writes a row to the tsv
def out(language, force, ur, nodes, outputfilename, test):
    if len(nodes)>24 and isinstance(nodes, list):
        print("why are there "+str(len(nodes))+" nodes in this list...")
        return
    with open(outputfilename, 'a') as f:
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
                    #print("start CP: ")
                    for x in n.daughters:
                        pass
                        #print(x.name, end=", ")
                        #print(x.null, end=", ")
                    #print("start expansion:")
                    row = expand(n, row)
        #row.append('\n')
        output.writerow(row)
        # if test == True:
        #     print("\n")
        #     for x in row:
        #         print(x, end='')
        f.close()
    return
 
# Adds the node.name to the row that will be written to the tsv file
def realize(node, row):
    row.append(node.name)
    return row

#Adds .tsv to the outputfile name if the user didn't put it in.  ###NOW OBSOLETE
def tsvcheck(filename):
    if ".tsv" not in filename:
        filename += ".tsv"
    return filename

def output_final_count(tree_count, outputfoldername):
    print(
        "\nAssessed "
        + str(tree_count)
        + " trees and wrote them to the '"
        + outputfoldername
        + "' series\n"
    )
