import os
from .ind_variables import *

# This test compares the SR output of the preceding script against a list of licit, known SRs
# found in the test.txt file
def test(outputfoldername, limited_UR_list):
    outcome         = ""
    fail_count      = 0
    failure         = False
    #t               = open(testfilename, 'r').readlines()
    #test_count      = len(t)
    output_name     = str(outputfoldername)

    test_lines      = test_SRs()
    test_count      = len(test_lines)
    # for line in t:
    #     test_lines.append(line.split())


    

    output_lines    = []
    output_count    = 0
    file_number = os.listdir(outputfoldername)
    for file in file_number:
        outputfilename  = outputfoldername+"/"+str(file)
        o               = open(outputfilename, 'r').readlines()
        output_count   += len(o)
        for line in o:  
            output_lines.append(line.split())
            #print(line)
            #Check for PP-->P O3
            '''
            if "parseable" not in line:
                if "PP" in line:
                    assert "O3" in line, "PP is present in UR, but O3 is missing from SR"
            assert l_split[16] == "SR:"
            if "PP" in l_split[0:16]:
                assert "O3" in l_split[16:31]
            '''

    fail_list = []
    for test in test_lines:
        if test in output_lines:
            pass
        else:
            fail_count += 1
            fail_list.append(test)
    
    if fail_count > 0:
        failure = True
        outcome = "Failure:  {f} out of {t} of the test lines are not present in the '{n}' output files!"
    if fail_count == 0:
        outcome = "Success:  It seems all {t} test lines are present in the {o} output lines in the '{n}' output files!"
    fail_list_outcome = "Failed test: {}"
    print(outcome.format(f=fail_count, t=test_count, o=output_count, n=output_name))
    for x in fail_list:
        print(fail_list_outcome.format(x))
    if failure == True:
        print("Remember, test failure could occur because of insufficient UR input, if a limited UR list is given to parent.")
        print("If the following URs do not contain the lexical items present in the test SRs, the test cannot succeed:")
        for x in limited_UR_list:
            print(x)
    '''
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price = 49))
    '''