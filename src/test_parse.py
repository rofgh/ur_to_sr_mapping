
testfilename    = "test.txt"
outputfilename  = "all_all.txt"
outcome         = "Test lines found in the output! Success!"
failed_line     = ""
with open(testfilename, 'r') as t:
    with open(outputfilename, 'r') as o:
        for test_line in t.readlines():
              while outcome == "Success! Test lines found in the output!":
                    if test_line in o.readlines():
                        pass
                    else:
                        outcome     = "Failure!  Test lines not found in the program output!"
                        failed_line = test_line
print(outcome)
print(failed_line)