# UR to SR mapping over 13 parameters
This project creates a mapping of meaninglessly ordered possible underlying lexical items (URs) to a surface order of words (SRs/SOWs), according to a hopefully scalable parameter set (a "language family") (there are 13 parameters that make up a language at the moment), and a static syntactic tree represented by a [Node class](https://github.com/rofgh/ur_to_sr_mapping/blob/1ab96bdabc231e07334c53806e0bcb91129e5752/src/nodes.py#L1).

## parent.py
Run this on the command line (python3)  (or 'make run' if make is installed)
This file takes four arguments, default=False/None in order to run a smaller domain, and begins the ur_to_sr_mapping code set.

```
$ python parent.py True True True outputfilename
$ make full

$ python parent.py
$ make run

```
1  
The first boolean argument determines whether all languages families are run (True) (n=8192) or whether only the [limited user-modified list](https://github.com/rofgh/ur_to_sr_mapping/blob/1ab96bdabc231e07334c53806e0bcb91129e5752/src/various.py#L4) is assessed (False) (e.g. [0,0,0,1,0,0,1,1,0,0,0,1,1]).

2  
The second argument determines whether all forces are assessed (True) or whether just one or two of the three are used (False) (Currently set to "D"eclarative in the [various.py scripts](https://github.com/rofgh/ur_to_sr_mapping/blob/1ab96bdabc231e07334c53806e0bcb91129e5752/src/various.py#L62))

3  
Limits the set of URs to assess (see [def activate_force()](https://github.com/rofgh/ur_to_sr_mapping/blob/efaf037f7c93b0af515be8cef8e0796705f152d4/src/various.py#L6)).  If a file is given, the script will run on a limited set of URs, which reduces the run time of the program, especially if all languages are being assessed.  Otherwise, this argument is False and all UR permutations are produced and mapped.

4  
Argument 4 is an output filename different from the default all_all.tsv  This deafult filename should only be used for the running of all parameter settings, all forces, and all URs.

This script also times how long each language family takes to produce, as well as the whole operation.

Running this could be replaced by 'make run' or its various permutations if make is installed.

### Github Folders:  
[src](https://github.com/rofgh/Hidden-Sin/tree/master/modules): these are the modules accessed by parent.py and sr_creator.py.  Also contains [UR_writer](https://github.com/rofgh/Hidden-Sin/tree/master/UR_writer):  Scripts that create the URs

[grabber](https://github.com/rofgh/Hidden-Sin/tree/master/grabber): this script pulls the SRs (and, optionally, the URs) form the original CoLAG data.  It is used for confirming correct production of this project.  

[S_F_Y_Data_Files](https://github.com/rofgh/Hidden-Sin/tree/master/S_F_Y_Data_Files): Self-explanatory  

[Misc](https://github.com/rofgh/Hidden-Sin/tree/master/Misc): Items that got put into the Notes shared doc, etc.  

[EDL Learner](https://github.com/rofgh/Hidden-Sin/tree/master/EDL%20Learner): Original 6 parameter script, etc.  

[Reference Papers](https://github.com/rofgh/Hidden-Sin/tree/master/Reference%20Papers):   
 
Our thoughts/description/notes/analysis/interpretation of the original SFY grammar and languages can be found [here](https://docs.google.com/document/d/1J_fS85IQWB9MPXB96ccHrKF_JHXn44iVyyemQOeFJQo/edit?usp=sharing)


