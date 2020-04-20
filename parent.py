'''
SR creator
takes the UR list, at all_URs.txt, for each one of them it runs the obj-maker, at obj-maker.py
producing, hopefully, a list of SRs/SOWs
'''

from src import sr_creator
import sys
from timeit import default_timer as timer

if __name__ == '__main__':
    start = timer()
    try:
        arg = sys.argv[1]
        if arg == 'True':
            all = True
        else:
            all = False
    except:
        all = False
    sr_creator.sr_creator(all)
    end = timer()
    total_time = end - start
    time_elapsed = "Total for this run: {tt:.2} seconds\n"
    print(time_elapsed.format(tt=total_time))



