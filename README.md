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

### Other:
obj_maker.py: old version of the SR_creator.py  Will probably soon be fully harvested and deleted  
all_all.txt: The output of SR_creator.py, will be created locally, as it has potential for being too large for github

## SR_creator.py
SR_creator.py creates SRs/SOWs for all the language-agnostic URs (created by all_URs.py), for whatever languages are selected:

There is a [boolean](https://github.com/rofgh/Hidden-Sin/blob/434a7e9c970c35f01e21bf55bc15415f6532940e/SR_creator.py#L12) to set to False if you want all languages, otherwise english = True and it will only produce for english, ie. [0,0,0,1,0,0,1,1,0,0,0,1,1] (Or some pre-entered list of languages).

NOT python2 compatible:
```bash
$ python3 SR_creator.py
```

SR Creator uses the following main modules:

nodes.py, which creates a list of node objects for each representation (i.e. a tree)
parameters.py, which applies each parameter setting according to the language that is provided

Our thoughts/description/notes for the languages can be found [here](https://docs.google.com/document/d/1J_fS85IQWB9MPXB96ccHrKF_JHXn44iVyyemQOeFJQo/edit?usp=sharing)


