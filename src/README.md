## SR_creator.py
SR_creator.py creates SRs/SOWs for all the language-agnostic URs (created by all_URs.py), for whatever languages are selected:

The boolean input to the parent script gets used [here](https://github.com/rofgh/Hidden-Sin/blob/434a7e9c970c35f01e21bf55bc15415f6532940e/SR_creator.py#L12) to set to True through an argument to the script if you want all languages, otherwise all = False and it will only produce for the limited language list found in [src/various.py](https://github.com/rofgh/ur_to_sr_mapping/blob/7ff5902a9bee21921103af8eb64e9ea210dd250c/src/various.py#L4), ie. [0,0,0,1,0,0,1,1,0,0,0,1,1].

True will run all combinations of parameter settings (~2secs/lang= 4.5 HOURS expected)
```bash
$ python3 SR_creator.py True True outputfilename
```

False or empty arg[1] will run only [limited user-modified list](https://github.com/rofgh/ur_to_sr_mapping/blob/1ab96bdabc231e07334c53806e0bcb91129e5752/src/various.py#L4) parameter settings (<2 seconds per language)

```bash
$ python3 SR_creator.py False True outputfilename
```

all_all.tsv currently looks like:
```bash
0000000000100	D	S	Verb            SR:	Not parseable because of Parameter: 4: no topic and topic is obligatory			
0000000000100	D	S	Verb	Aux     SR:	Not parseable because of Parameter: 4: no topic and topic is obligatory			
0000000000100	D	S	Verb	Adv	    SR:	Not parseable because of Parameter: 4: no topic and topic is obligatory			
0000000000100	D	S	Verb	O1		SR:	Not parseable because of Parameter: 4: no topic and topic is obligatory
0001001100011	D	S	Verb            SR:	S	Verb
0001001100011	D	S	Verb	Aux		SR:	S	Aux	Verb
0001001100011	D	S	Verb	Adv	    SR:	S	Verb	Adv
0001001100011	D	S	Verb	O1		SR:	S	Verb	O1
0001001100011	D	S	Verb	PP		SR:	S	Verb	P	O3
0001001100011	D	S	Verb	Aux	Adv	SR:	S	Aux	Verb	Adv
0001001100011	D	S	Verb	Aux	O1	SR:	S	Aux	Verb	O1
0001001100011	D	S	Verb	Aux	PP	SR:	S	Aux	Verb	P	O3	
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

nodes.py, which creates a list of node objects for each representation (i.e. a static syntactic tree)  
parameters.py, which applies each parameter setting according to the "language family" that is provided  
URs.py, produces all the possible URs, language agnostic


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


