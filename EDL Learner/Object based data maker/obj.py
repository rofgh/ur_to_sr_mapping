

UR = []
class Node:
    def __init__(self, name, mother, laughter, raughter, lister, rister, phrase):
        self.name       = name
        self.mother     = mother
        self.laughter   = laughter
        self.raughter   = raughter
        self.lister     = lister
        self.rister     = rister
        self.phrase     = phrase
        self.null       = True
        UR.append(self)

S   = Node("S",     None,   None,   None,   None,   None)

V   = Node("V",     None,   None,   None,   None,   None)
O1  = Node("O1",    Vbar,   None,   V,      O2,     IP)
O2  = Node("O2",    Vbar,   None,   O1,     PP,     IP)
PP  = Node("PP",    Vbar,   P,      O3,     O2,     Adv,    IP)


