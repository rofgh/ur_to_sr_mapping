'''
Test that the app can run
'''

from src            import sr_creator
from src.timeme        import *
import sys




if __name__ == '__main__':
    sr_creator.sr_creator(False, False, start(), False, "test_output.tsv")



