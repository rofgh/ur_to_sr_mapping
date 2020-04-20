
from .nodes      import nodes
from .parameters import apply_parameters
from .URs     import all_URs
from .various    import *
from .           import test_parse

def sr_creator(all):
    # runs the UR_writing script, creating .txt files for each force
    all_URs()
    tree_count = 0
    open("all_all.txt")
    for language in languages(all):
        # runs through the list of forces
        for force in forces():
            # returns list of lists, padded to 14 items (i.e. the most lexical items possible)
            all_URs_ = activate_force(force)
            # for each UR in this force's list of URs
            for ur in all_URs_:
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