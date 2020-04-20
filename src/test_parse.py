
def test():
    testfilename    = "test.txt"
    outputfilename  = "all_all.txt"
    outcome         = ""
    failed_line     = ""
    fail_count      = 0
    total_count     = 0
    total_fail_count= 0
    with open(testfilename, 'r') as t:
        with open(outputfilename, 'r') as o:
            total_count         = len(o.readlines())
            for test_line in t.readlines():
                total_fail_count += 1
                if test_line in o.readlines():
                    pass
                else:
                    fail_count += 1
    if fail_count > 0:
        outcome = "Failure:  {fc} out of {tfc} of the test lines are not present in the output!"
    if fail_count == 0:
        outcome = "Success:  It seems all {tc} the test lines are present in the {tc} output lines!"

    print(outcome.format(fc= fail_count, tfc=total_fail_count, tc=total_count))
    '''
    txt = "For only {price:.2f} dollars!"
    print(txt.format(price = 49))
    '''