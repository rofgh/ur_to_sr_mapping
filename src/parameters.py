'''
#3:
When do nodes become null = False?  It must happen before, for example, 
the NullTop and NullSub parameters disallow this, eh?

#4:
Does it work to make [+WH] a daughter of it's attachment node
and it will always get printed to the right of that node?  YES, I THINK SO...

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

#7
Does +wh need to be in the UR?  I think for now I will put it and 't' in.

#8
Why do I see questions [+wh][+wa], but no questions with [+wa][-wh] nor  [-wa][+wh]??

#9
When does the top move to the SpecCP node?  Because it has to be after the
prep-stranding parameter takes effect, or else the PP will all move no matter what....
Maybe just, if on and O3 is topicalized it turns PP. == True
And bifurcates in order to make one pied piping and one stranding case
IDEA:  PP gets the topicalizer, then parameter9 bifurcates and moves it to just O3?

#10
How to deal with the finiteness problem?  verbs left in the VP can't be
realized unless affix hopping happens.

Problem to revisit, am I doing this efficiently?:
Currently able to run one sentence for each language setting,
but how to run all the different URs within each language??
Parameter functions turn on or off everything, and then the next step is to step through each possible 
UR within that?
-->>  process_parameters produces all the URs for a language?

'''
import copy
def apply_parameters(PFN):
    # list of possible nodes lists *2 for each parameter that may add another list 
    l_of_l_of_nodes = []
    '''
    #First two, which happen for all forces
    for x in range(1,3):
        func = "Parameter"+str(x)+"(Pa["+str(Pa[x])+"], headedness_values)"
        eval(func)
    if force =! "I":
    #Third one, last of headedness
    for x in range(3,4):
        func = "Parameter"+str(x)+"(Pa["+str(Pa[x])+"], headedness_values)"
        eval(func)

    #Other ten, which no longer need the headedness
    for x in range(4,len(Pa)):
        func = "Parameter"+str(x)+"(Pa["+str(Pa[x])+"], UR)"
        eval(func)
    '''
    def move_topic(nodes):
        for n in nodes:
            if n.name == "CP":
                CP = n
        for n in nodes:
            if n.top == True:
                n.mother = CP
        return nodes

    def no_parse():
        return "Not parseable"

    def filler():
        return UR

    def ItoC(node):
            node.mother = Cbar
            node.phrase = "CP"

    def VtoI(node):
            node.mother = IP


    def set_head_position(PFN, headedness_values):
        for node in PFN[2]:
            if node.name not in ["CP", "-wa"]:
                assert node.phrase in ["SP","CP","IP"], [node.name, node.phrase]
                if node.phrase == "SP":
                    node.pos = headedness_values[0]
                if node.phrase == "IP":
                    node.pos = headedness_values[1]
                if node.phrase == "CP":
                    node.pos = headedness_values[2]
        return PFN
                
    def get_daughters(UR):
        for x in UR:
            if x.mother:
                y = x.mother
                y.daughters.append(x)
            else:
                pass
        return UR

    def if_on(value):
        pass
                

    ########################################### PARAMETERS ###########################################
    ########################################### HEADEDNESS PARAMETERS ###
    ### PARAMETER 1 ### ONLY AFFECTS HEADEDNESS OF NODES WITHIN SP (i.e. S)
    def Parameter1(PFN, h_v):
        value             = PFN[0][0]
        force             = PFN[1]
        UR                = PFN[2]
        if value == 0:
            h_v[0] = "L"
        if value == 1:
            h_v[0] = "R"
        return h_v

    ### PARAMETER 2 (Pa[1]) ###  ONLY AFFECTS HEADEDNESS OF NODES WITHIN IP
    def Parameter2(PFN, h_v):
        value             = PFN[0][1]
        force             = PFN[1]
        UR                = PFN[2]
        if value == 0:
            h_v[1] = "L"
        if value == 1:
            h_v[1] = "R"
        return h_v

    ### PARAMETER 3 (Pa[2]) ### ONLY AFFECTS HEADEDNESS OF NODES WITHIN CP
    # ka or a QInv/ItoC Aux/Verb are the only things that move for this parameter
    # If Pa[2]==1 and Pa[10]==1 and Aux == True: Aux will be CP final (and necessarily sentence final)
    def Parameter3(PFN, h_v):
        value             = PFN[0][2]
        force             = PFN[1]
        UR                = PFN[2]
        if value == 0:
            h_v[2] = "L"
        if value == 1:
            h_v[2] = "R"
        return h_v

########################################### EXISTENTIAL PARAMETERS ###
    ### PARAMETER 4 (Pa[3]) ### OptTop
    def Parameter4(PFN):
        value             = PFN[0][4]
        if value == 0:
            '''
            Topic is obligatory (something from top_nodes MUST move to Spec,CP)
            if UR does not have topic in it:
                no_parse()
            if UR does have a topic:
                continue with this node
            for x in top_nodes:
                attach -wa, set each one as daughter of the CP, then produce an SR
                Could this just be done by adding -wa to the NAME of the topicalized node?
                If there is a Spec,CP, attach -wa to it.
            '''
            return PFN
        # The following setting should have more SRs if they all get realized...
        if value == 1:
            '''
            Topic is optional (Can we just leave it off?)
            Same as above plus no topics?
            '''
            return PFN

    def Parameter5(PFN):
        value             = PFN[0][4]
        ### PARAMETER 5 (Pa[4]) ### Null Subject
        # The other way to code this is to add Null Subject to the UR, 
        # but how would that work for Null Topic?
        if value == 0:
            '''
            for x in UR:
                if x.name == "S":
                    x.null = False
            '''
            pass
        # The following setting should have more SRs if they all (i.e. null and non-null) get realized...
        if value == 1:
            # S can be null or not
            ###
            # Run another version of this UR/Parameter set, with null sub off:
            unnull_sub_PFN             = copy(PFN)
            unnull_sub_PFN[0][4]       = 0

            l_of_l_of_nodes.append(do_it(unnull_sub_PFN))
            ###
            for x in PFN[2]:
                if x.name == "S":
                    x.null = True
        return PFN

    

    ### PARAMETER 6 (Pa[5]) ### Null Topic
    #No null topic
    def Parameter6(PFN):
        assert isinstance(PFN, list), PFN
        assert isinstance(PFN[0], list), PFN
        value             = PFN[0][5]
        if value == 0:
            # topic is always realized, so:
            pass
        if value == 1:
            #Excluding the sentences created by this setting being off, above, this language will create
            #only Obligatory NullTop, unless changed a bit:
            #Whichever word is the topic:
            #TOPIC can be null or not
            ###
            # Run another version of this UR/Parameter set, with null top off:
            unnull_top_PFN             = copy(PFN)
            unnull_top_PFN[0][5]       = 0

            l_of_l_of_nodes.append(do_it(unnull_top_PFN))

            for x in PFN[2]:
                if x.mother == "S":
                    x.null = True
        return PFN


########################################### MOVEMENT PARAMETERS ###
    ### PARAMETER 7 (Pa[6]) ### Wh-Movement
    #Wh-in situ
    def Parameter7(PFN):
        value             = PFN[0][6]
        if value == 0:
            pass
        # [+WH] word goes to Spec,CP (NOT Spec,C') (NOT AFFECTED BY CP HEADEDNESS)
        if value == 1:
            '''
            if TOPIC != WH:
                #ERRORORORORO
                pass
            '''
            '''
            for x in PFN[2]:
                if x.daughter == Wh:
                    x.mother = CP
            '''
            pass
        return PFN

    ### PARAMETER 8 (Pa[7]) ### Preposition Stranding
    def Parameter8(PFN):
        value                = PFN[0][7]
        if value == 0:
            # P is topicalized (Never O3), PP must move as a group
            pass
        if value == 1:
            # O3 is topicalized (Never P), P does not have to move
            pied_piping_PFN             = copy.copy(PFN)
            pied_piping_PFN[0][7]       = 0

            l_of_l_of_nodes.append(do_it(pied_piping_PFN))

            for x in PFN[2]:
                if x.name == "PP":
                    if x.inUR == True:
                        if x.top == True:
                            for n in PFN[2]:
                                if x.name == "O3":
                                    x.top = True
                                else:
                                    x.top = False
        return PFN

    ### PARAMETER 9 (Pa[8]) ### Topic Marking
    def Parameter9(PFN):
        value                = PFN[0][8]
        if value == 0:
            # wa is already null, so skip
            pass

        if value == 1:
            #if there is a topicalized item, attach [+WA] to it
            for x in PFN[2]:
                if x.name == "-wa":
                    x.null = False
        return PFN
            
    ### PARAMETER 10 (Pa[9]) ### VtoI Movement
    def Parameter10(value):
        if value == 0:
            #If off, no movement occurs
            pass
        if value == 1:
            #If on, Verb tries to move to Spec,IP, unless Aux already occupies this node
            pass
            '''
            For current nodes:
                if Aux.inUR:
                    pass
                else:
                    VtoI(Verb)
            '''
        return PFN

    ### PARAMETER 11 (Pa[10]) ### ItoC Movement
    def Parameter11(PFN):
        value             = PFN[0][10]
        if value == 0:
            pass
        if value == 1:
            # +ItoC invalidates the need for P13 so we can just turn it off
            # This requires a base-generated Aux or a VtoI Verb
            # If no BG Aux
            for x in PFN[2]:
                if x.name == "Aux":
                    if x.inUR == False:
                        if PFN[0][9] == 0:
                            # Not parseable
                            PFN[2] = no_parse()
                        else:
                            for x in PFN[2]:
                                if x.name == "Verb":
                                    assert x.mother == IP, "Verb didn't move"
                                    ItoC(x)
            #BG Aux
                    else:
                        assert Aux.mother == IP, "Aux already moved?"
                        ItoC(Aux)
        return PFN
             
    ### PARAMETER 12 (Pa[11]) ### Affix Hopping
    # Does not allow Verb to stay in VP without an outside Aux
    def Parameter12(PFN):
        value             = PFN[0][11]
        if value == 0:
            pass
            '''
            if Aux.inUR == True:
                return PFN
            if Aux.inUR == False:
                # not parseable
                PFN[2] = no_parse()
                return PFN
            '''
        #  Allows Verb to take finiteness inside the VP
        if value == 1:
            if PFN[0][9] == 1:
                # Not parseable
                PFN[2] = no_parse()
                pass
            else:
                pass
        return PFN

    ### PARAMETER 13 (Pa[12]) ### Q-Inv  (i.e. ItoC for Qs)
    def Parameter13(PFN):
        value             = PFN[0][12]
        P10               = PFN[0][10]
        if P10 == 1:
            value = 0
        if value == 0:
            if P10 == 0:
                # ka appears only in languages where P11 and P13 are off
                for x in PFN[2]:
                    if x.name == "ka":
                        x.null = False
            else:
                pass
        if value == 1:
            # This requires a base-generated Aux or a VtoI Verb
            # If no BG Aux
            '''
            if Aux.inUR == False:
                if Pa[9] == 0:
                    # Not parseable
                    PFN[2] = no_parse()
                    return PFN
                else:
                    assert V.mother == IP, "Verb didn't move up, so can't continue"
                    ItoC(V)
            #BG Aux
            else:
                assert Aux.mother == IP, "Aux already moved?"
                ItoC(Aux)
            '''
        return PFN

    #assert len(Pa) == 13
    #assert isinstance(Pa, list)

    def do_it(PFN):
        Pa                = PFN[0]
        force             = PFN[1]
        UR                = PFN[2]

        headedness_values = [None,None,None]
        headedness_values = Parameter1(PFN, headedness_values)
        headedness_values = Parameter2(PFN, headedness_values)
        # If imperative, no other parameters come into play, so we can exit
        # with only 1 SOW/SR possibility
        if force == "I":
            PFN = set_head_position(PFN, headedness_values)
            #no other parameters come into play, so exit
            return PFN[2]
        headedness_values = Parameter3(PFN, headedness_values)
        # all headedness parameters set, the positions can be 
        PFN = set_head_position(PFN, headedness_values)
        while PFN[2] != "Not parseable":
            PFN  = Parameter4(PFN)
            PFN  = Parameter5(PFN)
            PFN  = Parameter6(PFN)
            PFN  = Parameter7(PFN)
            PFN  = Parameter8(PFN)
            PFN  = Parameter9(PFN)
            PFN = Parameter10(PFN)
            PFN = Parameter11(PFN)
            # Parameter 11 being on invalidates the need for Parameter 13 to be assessed
            PFN = Parameter12(PFN)
            if PFN[1] == "D":
                PFN[2] = move_topic(PFN[2])
                return PFN[2]
            Parameter13(PFN) 
            PFN[2] = move_topic(PFN[2])
        return PFN[2]


    l_of_l_of_nodes.append(do_it(PFN))
    return l_of_l_of_nodes