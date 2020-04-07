# Hidden-Sin
The main script is SR_creator.py, which accesses the other modules in the Modules folder.

### Folders:  
[grabber](https://github.com/rofgh/Hidden-Sin/tree/master/grabber): this script pulls the SRs (and, optionally, the URs) form the original CoLAG data  
[modules](https://github.com/rofgh/Hidden-Sin/tree/master/modules): these are the modules used by SR_creator.py  
[S_F_Y_Data_Files](https://github.com/rofgh/Hidden-Sin/tree/master/S_F_Y_Data_Files): Self-explanatory  
[Misc](https://github.com/rofgh/Hidden-Sin/tree/master/Misc): Items that got put into the Notes shared doc, etc.  
[EDL Learner](https://github.com/rofgh/Hidden-Sin/tree/master/EDL%20Learner): Original 6 parameter script, etc.  
[Reference Papers](https://github.com/rofgh/Hidden-Sin/tree/master/Reference%20Papers):   
[UR_writer](https://github.com/rofgh/Hidden-Sin/tree/master/UR_writer):  Scripts that create the URs for the SR_creator, these are combined in the URs.py script in the modules folder  

## SR_creator.py
SR_creator.py creates SRs/SOWs for all the language-agnostic URs (created by all_URs.py), for whatever languages are selected:

There is a [boolean](https://github.com/rofgh/Hidden-Sin/blob/434a7e9c970c35f01e21bf55bc15415f6532940e/SR_creator.py#L16) in def languages() to set to True through an argument to the script if you want all languages, otherwise all = False and it will only produce for english, ie. [0,0,0,1,0,0,1,1,0,0,0,1,1] (Or some pre-entered [list](https://github.com/rofgh/Hidden-Sin/blob/434a7e9c970c35f01e21bf55bc15415f6532940e/SR_creator.py#L29) of languages).

```bash
$ python3 SR_creator.py True
```
OR
```bash
$ python3 SR_creator.py
```
True will run all languages (ENTER EST TIME HERE)
False or empty arg[1] will run only English parameters (ENTER EST TIME HERE)

SR Creator uses the following main modules:

nodes.py, which creates a list of node objects for each representation (i.e. a tree)
parameters.py, which applies each parameter setting according to the language that is provided
URs.py, which should be run prior to running SR_creator, as it needs to produce .txt files that SR_c will access

### Other:
obj_maker.py: old version of the SR_creator.py  Will probably soon be fully harvested, obsolete, and deleted  
all_all.txt: The output of SR_creator.py, will be created locally, as it has potential for being too large for github

Our thoughts/description/notes/analysis/interpretation of the original SFY grammar and languages can be found [here](https://docs.google.com/document/d/1J_fS85IQWB9MPXB96ccHrKF_JHXn44iVyyemQOeFJQo/edit?usp=sharing)


