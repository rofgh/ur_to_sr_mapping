'''
SR creator
takes the UR list, at all_URs.txt, for each one of them it runs the obj-maker, at obj-maker.py
producing, hopefully, a list of SRs/SOWs
'''

from obj_maker  import produce
from nodes      import nodes
from parameters import apply_parameters

# generates all the language possibilities
def languages(english=True):
    # FOR ALL LANGUAGES
    if english == False:
        for x in range(0, 8192):
            language = []
            for digit in format(x, '013b'):
                if digit == '0':
                    language.append(0)
                if digit == '1':
                    language.append(1)
            yield language
    ### English only: (Or add other specific languages)
    if english == True:
        english = [[0,0,0,1,0,0,1,1,0,0,0,1,1]]
        for x in english:
            yield x

# selects a illocutionary force and produces all the possible URs for that force
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
    with open("all_all.txt", 'w') as f:
        for language in languages():
            for force in forces():
                all_URs = activate_force(force)
                for ur in all_URs:
                    node = nodes(ur)
                    node = apply_parameters(language, force, node)
                    if node != "Not parseable!":
                        #SR = produce(language, force, ur, nodes)
                        print("Hmmm")
                        pass
                    else:
                        SR = node
                    for dig in language:
                        f.write(str(dig)+"")
                    f.write("\t"+force+"\t")
                    f.write(ur)
                    #f.write(ur+"\t")
                    #f.write(SR)

