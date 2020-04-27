# UR to SR mapping over 13 parameters
This project creates a mapping of possible underlying lexical items (UR) to a surface order of words (SR/SOW), according to 13 binary parameters and a static syntactic tree.
USES Python3

## parent.py
Run this on the command line
Takes two arguments, default=False, and begins the ur_to_sr_mapping code
```
$ python parent.py True True
```
The first boolean argument determines whether all possible languages are run (True) or whether only the limited user-modified list is assessed (False).

The second argument determines whether all forces are assessed (True) or whether just one or two of the three possible forces are assessed (False) (Currently set to "D"eclarative)

Also times the whole operation. ()

Running this could be replaced by 'make run' if make is installed.


## parent.py
Run this on the command line
Takes two arguments, default=False, and begins the ur_to_sr_mapping code
```
$ python parent.py True True
```
The first boolean argument determines whether all possible languages are run (True) or whether only the limited user-modified list is assessed (False).

The second argument determines whether all forces are assessed (True) or whether just one or two of the three are used (False) (Currently set to "D"eclarative)

Also times the whole operation.

Running this could be replaced by 'make run' if make is installed.


## SR_creator.py
SR_creator.py creates SRs/SOWs for all the language-agnostic URs (created by all_URs.py), for whatever languages are selected:

The boolean input to the parent script gets used [here] (https://github.com/rofgh/Hidden-Sin/blob/434a7e9c970c35f01e21bf55bc15415f6532940e/SR_creator.py#L12) to set to True through an argument to the script if you want all languages, otherwise all = False and it will only produce for the limited language list found in [src/various.py](https://github.com/rofgh/ur_to_sr_mapping/blob/7ff5902a9bee21921103af8eb64e9ea210dd250c/src/various.py#L4), ie. [0,0,0,1,0,0,1,1,0,0,0,1,1].

True will run all languages (ENTER EST TIME HERE)

False or empty arg[1] will run only English parameters (1 second)


all_all.txt currently looks like (No SRs are being printed currently):
```bash
0001001000011	D	S	Verb													SR:	
0001001000011	D	S	Verb													SR:	
0001001000011	D	S	Verb	Aux												SR:	
0001001000011	D	S	Verb	Adv												SR:	
0001001000011	D	S	Verb	O1												SR:	
0001001000011	D	S	Verb	PP												SR:	
0001001000011	D	S	Verb	Aux	Adv											SR:	
0001001000011	D	S	Verb	Aux	O1											SR:	
0001001000011	D	S	Verb	Aux	PP											SR:	
0001001000011	D	S	Verb	Adv	O1											SR:	
0001001000011	D	S	Verb	Adv	PP											SR:	
0001001000011	D	S	Verb	O1	O2											SR:	
0001001000011	D	S	Verb	O1	PP											SR:	
0001001000011	D	S	Verb	Aux	Adv	O1										SR:	
0001001000011	D	S	Verb	Aux	Adv	PP										SR:	
0001001000011	D	S	Verb	Aux	O1	O2										SR:	
```

At the end of the run, this script will run a test that compares the SR_creator output to a test.txt which contains a list of UR-SR maps known/expected to be produced by the creator.

There are two outcomes from the test:
```
Failure!  Test lines not found in the output!
```
OR
```
Success! Test lines found in the output!
```




### SR Creator accesses the following modules:

nodes.py, which creates a list of node objects for each representation (i.e. a tree)  
parameters.py, which applies each parameter setting according to the language that is provided  
URs.py, which should be run prior to running SR_creator, as it needs to produce .txt files that SR_c will access  


### Folders:  
[grabber](https://github.com/rofgh/Hidden-Sin/tree/master/grabber): this script pulls the SRs (and, optionally, the URs) form the original CoLAG data  
[modules](https://github.com/rofgh/Hidden-Sin/tree/master/modules): these are the modules used by SR_creator.py  
[S_F_Y_Data_Files](https://github.com/rofgh/Hidden-Sin/tree/master/S_F_Y_Data_Files): Self-explanatory  
[Misc](https://github.com/rofgh/Hidden-Sin/tree/master/Misc): Items that got put into the Notes shared doc, etc.  
[EDL Learner](https://github.com/rofgh/Hidden-Sin/tree/master/EDL%20Learner): Original 6 parameter script, etc.  
[Reference Papers](https://github.com/rofgh/Hidden-Sin/tree/master/Reference%20Papers):   
[UR_writer](https://github.com/rofgh/Hidden-Sin/tree/master/UR_writer):  Scripts that create the URs for the SR_creator, these are combined in the URs.py script in the modules folder  

### Other:
obj_maker.py: old version of the SR_creator.py  Will probably soon be fully harvested, obsolete, and deleted  
all_all.txt: The output of SR_creator.py, will be created locally, as it has potential for being too large for github  

Our thoughts/description/notes/analysis/interpretation of the original SFY grammar and languages can be found [here](https://docs.google.com/document/d/1J_fS85IQWB9MPXB96ccHrKF_JHXn44iVyyemQOeFJQo/edit?usp=sharing)


