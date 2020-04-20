'''
SR creator
takes the UR list, at all_URs.txt, for each one of them it runs the obj-maker, at obj-maker.py
producing, hopefully, a list of SRs/SOWs
'''

from src import sr_creator
import sys



if __name__ == '__main__':
    open("all_all.txt", 'w')
    try:
        arg = sys.argv[1]
        if arg == 'True':
            all = True
        else:
            all = False
    except:
        all = False
    sr_creator.sr_creator(all)



