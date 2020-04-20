
def test():
    testfilename    = "test.txt"
    outputfilename  = "all_all.txt"
    outcome         = ""
    failed_line     = ""
    fail_count      = 0
    count           = 0
    with open(testfilename, 'r') as t:
        with open(outputfilename, 'r') as o:
            total_count = len(o.readlines())
            for test_line in t.readlines():
                if test_line in o.readlines():
                    pass
                else:
                    count += 1
    if count > 0:
        outcome = "Failure:  some of the test lines are not present in the output!"
    if count == 0:
        outcome = "Success:  It seems all the test lines are present in the output!"
    print(outcome)