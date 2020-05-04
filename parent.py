'''
Takes two arguments, default=False, and begins the ur_to_sr_mapping code
Also times the whole operation 
'''

from src import sr_creator
import sys
from src import timeme

if __name__ == '__main__':
    start_time = timeme.start()
    try:
        #For all languages or not
        arg = sys.argv[1]
        if arg == 'True':
            lang = True
        else:
            lang = False
    except:
        lang = False
    try:
        #For all forces or not
        arg2 = sys.argv[2]
        if arg2 == 'True':
            forces = True
        else:
            forces = False
    except:
        forces = False
    try:
        #Did the user put in a outputfilename?
        arg3 = sys.argv[3]
        outputfilename = arg3
    except:
        outputfilename = "all_all.tsv"
    sr_creator.sr_creator(lang, forces, start_time, outputfilename)
    timeme.end(start_time)
    



