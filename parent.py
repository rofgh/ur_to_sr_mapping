"""
Takes four arguments, default=False False False run, and begins the ur_to_sr_mapping code
Also times the whole operation 
"""

from src import sr_creator
import sys
from src import timeme
from src import test_parse
import os
import shutil

if __name__ == "__main__":
    start_time = timeme.start()
    # Boolean for All languages (True) versus only the list of desired languages (False)
    # gets sent to languages() from various.py
    try:
        arg = sys.argv[1]
        if arg == "True":
            lang = True
        else:
            lang = False
    except:
        lang = False
        

    # Boolean for All forces (True) versus only the list of desired forces (False)
    # gets sent to force_finder() in various.py
    try:
        arg2 = sys.argv[2]
        if arg2 == "True":
            forces = True
        else:
            forces = False
    except:
        forces = False

    # Are we using all URs (True) or a limited set (False)
    # gets sent to activate_force() in various.py
    try:
        arg3 = sys.argv[3]
        if arg3 == "True":
            test_URs = True
        else:
            test_URs = False
    except:
        test_URs = False

    # Did the user put in a output folder?
    try:
        arg4 = sys.argv[4]
        if arg4 == "False":
            outputfoldername = "run"
        else:
            outputfoldername = arg4
    except:
        outputfoldername = "run"

    # Create folder to hold output files
    if os.path.isdir(outputfoldername):
        shutil.rmtree(outputfoldername)
    os.mkdir(outputfoldername)
    # Send all to the SR_creator script
    sr_creator.sr_creator(start_time, lang, forces, test_URs, outputfoldername)
    # If all URs are not being used, run the test to ensure that the cataloged licit parses are present
    if test_URs == False:
        test_parse.test(False, outputfoldername)
    timeme.end(start_time)
