
def test():
    testfilename    = "test.txt"
    outputfilename  = "all_all.txt"
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


    for test in test_lines:
        if test in output_lines:
            pass
        else:
            fail_count += 1
    if fail_count > 0:
        print(test_lines)
        outcome = "Failure:  {fc} out of {tfc} of the test lines are not present in the output!"
    if fail_count == 0:
        outcome = "Success:  It seems all {tfc} test lines are present in the {tc} output lines!"

    print(outcome.format(fc=fail_count, tfc=test_count, tc=output_count))
    '''
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price = 49))
    '''