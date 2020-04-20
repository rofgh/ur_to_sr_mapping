'''
SR creator
takes the UR list, at all_URs.txt, for each one of them it runs the obj-maker, at obj-maker.py
producing, hopefully, a list of SRs/SOWs
'''

from src import sr_creator
import sys
from src import timer

if __name__ == '__main__':
    start = timer.start()
    try:
        arg = sys.argv[1]
        if arg == 'True':
            lang = True
        else:
            lang = False
    except:
        lang = False
    try:
        arg2 = sys.argv[2]
        if arg2 == 'True':
            forces = True
        else:
            forces = False
    except:
        forces = False
    sr_creator.sr_creator(lang, forces)
    timer.end(start)
    



