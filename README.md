# UR to SR mapping over 13 parameters
This project creates mappings of every possible combination of (meaninglessly ordered) underlying lexical items to a resultant surface order of words (SRs/SOWs/"a sentence").  Each "sentence" mapping is produced by applying a parameter set ("language family features") to a static syntactic tree, wherein each lexical item has a fixed birthplace, prescribed movement loci, and is either underlying null or present.

This project is intended to be used by an Expectation Maximization learning algorithm (Expectation Driven Learning (EDL)) as input data.  Working through each UR-to-SR mapping in a language family's data, the algorithm updates its beliefs about what language is being viewed.  This algorithm is essentially a proxy for human language learning under the principles and parameters model, in which the marginal addition of language data from each utterance updates a learner's assumptions about the language family they are learning, and the grammatical attributes of their language family.

Thus, this project represents an abstracted sample of language data that a human learner would encounter while learning a language, with the UR representing something like the semantically meaningful items and the SR representing the heard or produced utterance.

The parameters of the current project are based on the 13 outlined in a [Sakas & Fodor 2012 article](http://www.colag.cs.hunter.cuny.edu/pub/Sakas_Fodor_Disambiguating_prepub.pdf#24).  We wanted to plumb the structure of their parametric grammar, and produce a mapping that would be more appropriate for feeding to the EDL algorithm.

The language family set should be extendable/scalable by adding additional parameters in [src/parameters.py](https://github.com/rofgh/ur_to_sr_mapping/blob/04ee506608f7c58b81418987d333ec76d639e712/src/parameters.py#L1).  Depending on the format of this parameter, this will require the addition of syntactic tree lexical item(s), which would need to be reflected in [nodes.py](https://github.com/rofgh/ur_to_sr_mapping/blob/04ee506608f7c58b81418987d333ec76d639e712/src/nodes.py#L1) and changes to the [UR_writer](https://github.com/rofgh/Hidden-Sin/tree/master/UR_writer).  Essentially, scaling by another parameter requires some fluency in the script, but should be possible without changing any of the existing script.

See the [src readme](https://github.com/rofgh/ur_to_sr_mapping/blob/master/src/README.md) for more in depth descriptions of the code.

Our preliminary thoughts/description/notes/analysis/interpretation of the original SFY grammar and languages can be found [here](https://docs.google.com/document/d/1J_fS85IQWB9MPXB96ccHrKF_JHXn44iVyyemQOeFJQo/edit?usp=sharing)

## parent.py
Run this on the command line (python3)  (or 'make run' if make is installed, see [makefile](https://github.com/rofgh/ur_to_sr_mapping/blob/04ee506608f7c58b81418987d333ec76d639e712/Makefile#L1))  
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
Limits the set of URs to assess (see [various.py def activate_force()](https://github.com/rofgh/ur_to_sr_mapping/blob/efaf037f7c93b0af515be8cef8e0796705f152d4/src/various.py#L6)).  If a file is given, the script will run on a limited set of URs, which reduces the run time of the program, especially if all languages are being assessed.  Otherwise, this argument is False and all UR permutations are produced and mapped.

4  
Argument 4 is an output filename different from the default all_all.tsv  This deafult filename should only be used for the running of all parameter settings, all forces, and all URs.

This script also times how long each language family takes to produce, as well as the whole operation.


### Github Folders:  
[src](https://github.com/rofgh/Hidden-Sin/tree/master/src): these are the modules accessed by parent.py and sr_creator.py.  Also contains [UR_writer](https://github.com/rofgh/Hidden-Sin/tree/master/src/UR_writer):  Scripts that create the URs

[grabber](https://github.com/rofgh/Hidden-Sin/tree/master/grabber): this script pulls the SRs (and, optionally, the URs) form the original CoLAG data.  It is used for confirming correct production of this project.  

[S_F_Y_Data_Files](https://github.com/rofgh/Hidden-Sin/tree/master/S_F_Y_Data_Files): Self-explanatory  

[Misc](https://github.com/rofgh/Hidden-Sin/tree/master/Misc): Items that got put into the Notes shared doc, etc.  

[EDL Learner](https://github.com/rofgh/Hidden-Sin/tree/master/EDL%20Learner): Original 6 parameter script, etc.  

[Reference Papers](https://github.com/rofgh/Hidden-Sin/tree/master/Reference%20Papers):   
 



