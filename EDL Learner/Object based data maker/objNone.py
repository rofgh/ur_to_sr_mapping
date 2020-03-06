
def assess_language(Pa):
    UR = []
    class Node:
        def __init__(self, name, head, phrase, mother, real):
            self.name       = name
            self.head       = head
            self.phrase     = phrase
            self.mother     = mother
            self.real       = real
            self.daughters  = []
            self.pos        = None
            self.null       = True
            UR.append(self)

    CP      = Node(" CP", False, None, None, False)
    Cbar    = Node(" Cbar", False, CP, CP, False)
    ka      = Node(" ka", True, CP, Cbar, True)
    SP      = Node(" SP", False, CP, Cbar, False)
    wa      = Node(" wa", True, CP, Cbar, True)
    that    = Node(" that", True, CP, Cbar, False)
    Wh      = Node("[+WH]", False, CP, Cbar, True)
    S       = Node(" S", True, SP, SP, True)
    IP      = Node(" IP", False, SP, SP, False)
    Aux     = Node(" Aux", False, IP, IP, True)
    NegP    = Node(" NegP", False, IP, IP, False)
    Not     = Node(" not", True, IP, NegP, True)
    Nev     = Node(" never", True, IP, NegP, True)
    VP      = Node(" VP", False, IP, NegP, False)
    Adv     = Node(" Adv", True, IP, VP, True)
    Vbar3   = Node(" Vbar3", False, IP, VP, False)
    Vbar2   = Node(" Vbar2", True, IP, Vbar3, False)
    O2      = Node(" O2", False, IP, Vbar2, True)
    PP      = Node(" PP", False, IP, Vbar3, False)
    P       = Node(" P", True, IP, PP, True)
    O3      = Node(" O3", False, IP, PP, True)
    Vbar1   = Node(" Vbar1", True, IP, Vbar2, False)
    V       = Node(" Verb", True, IP, Vbar1, True)
    O1      = Node(" O1", False, IP, Vbar1, True)
    for x in UR:
        if x.mother:
            y = x.mother
            y.daughters.append(x)
        else:
            pass
                                        ### HEADEDNESS PARAMETERS ###
    ### PARAMETER 1 ### ONLY AFFECTS HEADEDNESS OF NODES WITHIN SP (i.e. S)
    sps = [x for x in UR if x.phrase == SP]
    # print("\nWHATS IN SP:")
    # [print(x.name) for x in sps]
    if Pa[0] == 0:
        for node in sps:
            if node.head == True:
                node.pos = "L"
            else:
                node.pos = "R"
    if Pa[0] == 1:
        for node in sps:
            if node.head == True:
                node.pos = "R"
            else:
                node.pos = "L"



    ### PARAMETER 2 ###  ONLY AFFECTS HEADEDNESS OF NODES WITHIN IP
    ips = [x for x in UR if x.phrase == IP]
    if Pa[1] == 0:
        for node in ips:
            if node.head == True:
                node.pos    = "L"
            else:
                node.pos    = "R" 

    if Pa[1] == 1:
        for node in ips:
            if node.head == True:
                node.pos    = "R"
            else:
                node.pos    = "L"
    # print("\nWHATS IN IP:")
    # [print(x.name,"\t", x.pos) for x in ips]


    ### PARAMETER 3 ### ONLY AFFECTS HEADEDNESS OF NODES WITHIN CP
    cps = [x for x in UR if x.phrase == CP]
    # print("\nWHATS IN CP:")
    # [print(x.name) for x in cps]
    if Pa[2] == 0:
        for node in cps:
            if node.head == True:
                node.pos = "L"
            else:
                node.pos = "R"
    if Pa[2] == 1:
        for node in cps:
            if node.head == True:
                node.pos = "R"
            else:
                node.pos = "L"






    for x in UR:
        x.null = False
    # V.null = False
    # P.null = False
    # O3.null= False
    # S.null = False
    # O1.null= False
    # O2.null= False
    # Adv.null = False
    # CP.null = False
    # that.null= False

        



    def expand(node):
        lis = node.daughters
        if len(lis) != 0:
            for x in lis:
                if x.pos == "L":
                    expand(x)
                if x.pos == "R":
                    pass
            for x in lis:
                if x.pos == "R":
                    expand(x)
                if x.pos == "L":
                    pass
        if len(lis) == 0:
            realize(node)

    def realize(node):
        if node.null == False:
            if node.real == True:
                print(node.name, end = '')
    
    expand(CP)
    print()
    print()
    '''


    f = expand(CP)
    for x in f:
        if x.pos == "L":
            realize(x)
            expand(x)
        if x.pos == "R":
            realize(x)
            expand(x)
    '''

if __name__ == '__main__':
    ### ALL THE PARAMETER SETTINGS ####
    for x in range(0, 8192):
        p_list = []
        for digit in format(x, '13b'):
            if digit == ' ':
                p_list.append(0)
            if digit == '0':
                p_list.append(0)
            if digit == '1':
                p_list.append(1)
        print("Language "+str(x+1)+": "+str(p_list))
        assess_language(p_list)
