
def test(filename):
    testfilename    = "test.txt"
    outputfilename  = filename
    outcome         = ""
    failed_line     = ""
    fail_count      = 0
    t               = open(testfilename, 'r').readlines()
    test_count      = len(t)

    test_lines      = []
    for line in t:
        test_lines.append(line.split())

    o               = open(outputfilename, 'r').readlines()
    output_count    = len(o)

    output_lines    = []
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
        outcome = "Failure:  {f} out of {t} of the test lines are not present in the output!"
    if fail_count == 0:
        outcome = "Success:  It seems all {t} test lines are present in the {o} output lines!"
    fail_list_outcome = "Failed test: {}"
    print(outcome.format(f=fail_count, t=test_count, o=output_count))
    for x in fail_list:
        print(fail_list_outcome.format(x))
    '''
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price = 49))
    '''