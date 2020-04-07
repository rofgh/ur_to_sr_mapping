## grabber.py
The grabber script allows us to look at the SRs and associated bracketed UR trees for specific parameter settings of the CoLAG languages.

The [flat.txt file](http://www.colag.cs.hunter.cuny.edu/grammar/data/COLAG_2011_flat.zip) needs to be
saved in your branch's SRs folder, as it is too big to put on GitHub

Example for running script (python 2 & 3 compatible):

```bash
$ python grabber.py 0001110001110 0 0
```

Arg1: 13 digit list of parameter settings (a list of all realizable setting combos is in [all_real_p.txt](https://github.com/rofgh/Hidden-Sin/blob/master/SRs/all_real_p.txt))\
Arg2: 0/1, whether you want UR bracketed representations to be printed ("_UR")\
Arg3: 0/1, whether you want the list to have gaps where the SRs are missing for that 
language (i.e. for that set of parameters) ("_gaps")

When you run the script it will produce a .txt file for that language with the parameter settings as the name, containing a tab delimited list of the SRs, sorted by the UR ID.

Arg2 off, Arg3 on:
```bash
UR #	ILLOC	SR	
0:	Q  	    Aux S Never Verb                                  	
1:                              	
2:	Q  	    Aux S Never Verb O1 O2
```

Arg2 on, Arg3 off:
```bash
UR #	ILLOC	SR	
0:	Q  	    Aux S Never Verb                                  	(CP[ILLOC DEC][+FIN]"Adv[+NULL][+TOPIC]"(Cbar[ILLOC DEC][+FIN][SLASH Adv](C[ILLOC DEC][+FIN]"Aux[+FIN]")(IP[ILLOC DEC][+FIN][SLASH Adv][SLASH Aux]"S"(Ibar[ILLOC DEC][+FIN][SLASH Adv][SLASH Aux](I[ILLOC DEC][+FIN][SLASH Aux]"Aux[+FIN][+NULL][SLASH Aux]")(NegP[SLASH Adv]"Never"(Negbar[SLASH Adv](VP[SLASH Adv](Vbar[SLASH Adv](V"Verb")"Adv[+NULL][SLASH Adv]"))))))))        132
2:	Q  	    Aux S Never Verb O1 O2                            	(CP[ILLOC DEC][+FIN]"Adv[+NULL][+TOPIC]"(Cbar[ILLOC DEC][+FIN][SLASH Adv](C[ILLOC DEC][+FIN]"Aux[+FIN]")(IP[ILLOC DEC][+FIN][SLASH Adv][SLASH Aux]"S"(Ibar[ILLOC DEC][+FIN][SLASH Adv][SLASH Aux](I[ILLOC DEC][+FIN][SLASH Aux]"Aux[+FIN][+NULL][SLASH Aux]")(NegP[SLASH Adv]"Never"(Negbar[SLASH Adv](VP[SLASH Adv](Vbar[SLASH Adv](V"Verb")"O1""O2""Adv[+NULL][SLASH Adv]"))))))))        132	
```

Our thoughts/description/notes for the languages can be found [here](https://docs.google.com/document/d/1J_fS85IQWB9MPXB96ccHrKF_JHXn44iVyyemQOeFJQo/edit?usp=sharing)


