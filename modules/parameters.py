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
def apply_parameters(Pa, force, UR):
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
    def no_parse():
        return "Not parseable"

    ###DELETABLE
    # def output(x):
    #     #print to terminal
    #     print(x)
    #     #print to output file:
    #     with open(out_filename, 'w') as f:
    #         f.write(x)

    def ItoC(node):
            node.mother = Cbar
            CP_nodes.append(node)
            IP_nodes.remove(node)

    def VtoI(node):
            node.mother = IP

    def set_head_position(UR, headedness_values):
        for node in UR:
            if node.phrase == SP:
                node.pos = headedness_values[0]
            if node.phrase == IP:
                node.pos = headedness_values[1]
            if node.phrase == CP:
                node.pos = headedness_values[2]
        return UR
                
    def get_daughters(UR):
        for x in UR:
            if x.mother:
                y = x.mother
                y.daughters.append(x)
            else:
                pass
        return UR

########################################### PARAMETERS ###########################################
########################################### HEADEDNESS PARAMETERS ###
    ### PARAMETER 1 ### ONLY AFFECTS HEADEDNESS OF NODES WITHIN SP (i.e. S)
    def Parameter1(value, h_v):
        if value == 0:
            h_v[0] = "L"
        if value == 1:
            h_v[0] = "R"
        return h_v

    ### PARAMETER 2 (Pa[1]) ###  ONLY AFFECTS HEADEDNESS OF NODES WITHIN IP
    def Parameter2(value, h_v):
        if value == 0:
            h_v[1] = "L"
        if value == 1:
            h_v[1] = "R"
        return h_v
    
    ###### Parameter settings aren't needed beyond here if Imperative
    if force == "I":
        return UR

    ### PARAMETER 3 (Pa[2]) ### ONLY AFFECTS HEADEDNESS OF NODES WITHIN CP
    # ka or a QInv/ItoC Aux/Verb are the only things that move for this parameter
    # If Pa[2]==1 and Pa[10]==1 and Aux == True: Aux will be CP final (and necessarily sentence final)
    def Parameter3(value, h_v):
        if value == 0:
            h_v[2] = "L"
        if value == 1:
            h_v[2] = "R"
        return h_v

    '''
########################################### EXISTENTIAL PARAMETERS ###
    ### PARAMETER 4 (Pa[3]) ### OptTop
    if Pa[3] == 0:
        Topic is obligatory (something from top_nodes MUST move to Spec,CP)
        for x in top_nodes:
            attach -wa, set each one as daughter of the CP, then produce an SR
            Could this just be done by adding -wa to the NAME of the topicalized node?
            If there is a Spec,CP, attach -wa to it.
    # The following setting should have more SRs if they all get realized...
    if Pa[3] == 1:
        Topic is optional (Can we just leave it off?)
        Same as above plus no topics?  
    '''

    '''
    ### PARAMETER 5 (Pa[4]) ### Null Subject
    
    if Pa[4] == 0:
        pass
    # The following setting should have more SRs if they all (i.e. null and non-null) get realized...
    if Pa[4] == 1:
        # S can be null or not
        S.null = True
    '''

    '''
    ### PARAMETER 6 (Pa[5]) ### Null Topic
    #No null topic
    if Pa[5] == 0:
        # topic is always realized, so:
        pass
    if Pa[5] == 1:
        Excluding the sentences created by this setting being off, above, this language will create
        only Obligatory NullTop, unless changed a bit:
        #Whichever word is the topic:
            #TOPIC can be null or not
            x.null = True
    '''
########################################### MOVEMENT PARAMETERS ###
    '''
    ### PARAMETER 7 (Pa[6]) ### Wh-Movement
    #Wh-in situ
    if Pa[6] == 0:
        pass
    # [+WH] word goes to Spec,CP (NOT Spec,C') (NOT AFFECTED BY CP HEADEDNESS)
    if Pa[6] == 1:
        if TOPIC != WH:
            #ERRORORORORO
            pass
        for x in nodes:
            if x.daughter == Wh:
                x.mother = CP
    '''

    '''
    ### PARAMETER 8 (Pa[7]) ### Preposition Stranding

    IDEA:  PP gets the topicalizer, then this parameter moves it to just O3 if need be?
    # If PP is topicalized:
    # P is topicalized (Never O3), PP must move as a group
    if Pa[7] == 0:
        pass
    # O3 is topicalized (Never P), P does not have to move 
    if Pa[7] == 1:
        O3.top  = True
    '''

    ### PARAMETER 9 (Pa[8]) ### Topic Marking
    if Pa[8] == 0:
        wa.null = True
    if Pa[8] == 1:
        #if there is a topicalized item, attach [+WA] to it
        wa.null = False

    '''
    ### PARAMETER 10 (Pa[9]) ### VtoI Movement
    if Pa[9] == 0:
        #If off, no movement occurs
        pass
    if Pa[9] == 1:
        #If on, Verb tries to move to Spec,IP, unless Aux already occupies this node
        For current nodes:
            if Aux.inUR:
                pass
            else:
                VtoI(Verb)
    '''
    ### PARAMETER 11 (Pa[10]) ### ItoC Movement
    if Pa[10] == 0:
        pass
    if Pa[10] == 1:
        # +ItoC invalidates the need for P13 so we can just turn it off
        pa[13] = 0
        # This requires a base-generated Aux or a VtoI Verb
        # If no BG Aux
        if Aux.inUR == False:
            if Pa[9] == 0:
                # Not parseable
                return no_parse()
            else:
                assert Verb.mother == IP, "Verb didn't move"
                ItoC(V)
        #BG Aux
        else:
            assert Aux.mother == IP, "Aux already moved?"
            ItoC(Aux)
    '''      
    ### PARAMETER 12 (Pa[11]) ### Affix Hopping
    # Does not allow Verb to stay in VP without an outside Aux
    if Pa[11] == 0:
        if Aux.inUR == True:
            pass
        if Aux.inUR == False:
            # not parseable
            return no_parse()
    #  Allows Verb to take finiteness inside the VP
    if Pa[11] == 1:
        if Pa[9] == 1:
            # Not parseable
            return no_parse()
        else:
            pass
    '''
    ##### Parameter settings aren't needed after here for Declaratives
    if force == "D":
        return UR

    ### PARAMETER 13 (Pa[12]) ### Q-Inv  (i.e. ItoC for Qs)

    if Pa[12] == 0:
        if Pa[10] == 0:
            # ka appears only in languages where P11 and P13 are off
            ka.null = False
        else:
            pass
    if Pa[12] == 1:
        # This requires a base-generated Aux or a VtoI Verb
        # If no BG Aux
        if Aux.inUR == False:
            if Pa[9] == 0:
                # Not parseable
                return no_parse()
            else:
                assert V.mother == IP, "Verb didn't move up, so can't continue"
                ItoC(V)
        #BG Aux
        else:
            assert Aux.mother == IP, "Aux already moved?"
            ItoC(Aux)

    assert len(Pa) == 13
    assert isinstance(Pa, list)

    headedness_values = [None,None,None]
    headedness_values = Parameter1(Pa[0], headedness_values)
    headedness_values = Parameter1(Pa[1], headedness_values)
    
    if force == "I":
        UR = set_head_position(UR, headedness_values)
        #no other parameters come into play, so exit
        return UR

    headedness_values = Parameter1(Pa[2], headedness_values)
    UR = set_head_position(UR, headedness_values)
    nodes = Parameter4(Pa[3])
    nodes = Parameter5(Pa[4])
    nodes = Parameter6(Pa[5])
    nodes = Parameter7(Pa[6])
    nodes = Parameter8(Pa[7])
    nodes = Parameter9(Pa[8])
    nodes = Parameter10(Pa[9])
    nodes = Parameter11(Pa[10])
    nodes = Parameter12(Pa[11])
    if force == "D":
        return UR
    Parameter13(Pa[12])
    return UR