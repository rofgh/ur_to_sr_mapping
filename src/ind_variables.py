# ind_variables.py
# Functions that create or store independent variables for entry into the parent.py script

#Which illocutionary forces to include in the mapping
def limited_forces_list():
    forces_list=[
        "D",
        #"I",
        "Q"

    ]

    return forces_list

# Which language families to include in the mapping
def limited_languages_list():
    languages_list = [
    [0,0,0,0,0,0,0,0,1,0,0,0,0],    #Topic Marking
    [0,0,0,1,0,0,1,1,0,0,0,1,1],    #English
    [0,0,0,0,0,0,0,0,0,0,0,0,0],    #All off
    [0,0,0,0,0,0,0,0,0,0,0,0,1],    #All off, but obl Q inversion
    [0,0,0,0,0,0,0,0,0,0,0,1,0],    #All off, but Affix hopping
    [0,0,0,0,0,0,0,0,0,0,1,0,0],    #All off, but ItoC movement
    [1,0,0,0,0,0,0,0,0,0,0,0,0],    #All off, but Left Subject pos
    [0,1,0,0,0,0,0,0,0,0,0,0,0],    #All off, but Left IP pos
    [0,1,0,1,0,0,0,0,0,0,0,0,0],    #All off, but Left IP pos and optTop
    [1,1,1,1,1,1,1,1,1,1,1,1,1],    #All on
    [0,0,0,1,1,1,0,0,1,0,0,0,0],    #OptTop, Null Top, Null Sub, Topic Marking
    [1,1,1,1,0,0,0,0,0,0,0,1,0],    #All Right Head, OptTop, Affix Hopping
    [1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1],
    ]
    return languages_list

# Which underlying representations to include in the mapping
def limited_UR_list():
    UR_list = [
        ['S','Verb'],	
        ['S','Verb','Aux']
    ]
    return UR_list

# Which licit SRs should the mapping verify
def test_SRs():
    test_lines = [
        ['0000000010000',	'D',	'S+t',	'Verb',	'Aux',	'SR:',	'S',	'[+wa]',	'Aux',	'Verb'  ],
        ['0001001100011',	'D',	'S',	'Verb',	'PP',	'SR:',	'S',	'Verb',	    'P',	'O3'    ],
        ['0001110010000',	'D',	'S',	'Verb',	'Aux',	'SR:',	'S',	'Aux',	    'Verb'          ],		
        ['0001110010000',	'D',	'S',    'Verb',	'Aux',	'SR:',	'Aux',	'Verb'                      ],	
    ]
    return test_lines
