# Hidden-Sin
 
## SRs/GRABBER
The grabber script allows us to look at the SRs for a specific set of parameter settings.

The [flat.txt file](http://www.colag.cs.hunter.cuny.edu/grammar/data/COLAG_2011_flat.zip) needs to be
saved in the SRs file, as it is too big to put on GitHub

Then the script is run by with the following:

```bash
$ python 0001110001110 0 0
```

Arg1 13 digit argument is the list of parameter settings\
Arg2 is whether you want UR bracketed representations to be printed\
ARg3 is whether you want the list to have gaps where the SRs are missing for that
language (i.e. for that set of parameters)
