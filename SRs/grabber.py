#INPUT: 0001110001110 0
#sys.argv[1]: parameter settings in binary form, thirteen digits long: "0001110001110" 
#sys.argv[2]: do you want to see the UR treelets?


#OUTPUT:  tab delimited text file with the parameter settings as the filename
# listing all the SR produced by the language, and the UR for each, if sys.argv[2] is on
# 
# 


import sys

para = sys.argv[1]
if len(para) != 13:
    print "\nWrong parameter settings length, it should be thirteen digits long! Try again!"
    exit()
try:
    URon = sys.argv[2]
except:
    print "did you enter a second argument?  Do you want to see the URs or not?"
    exit()
all = open("COLAG_2011_flat.txt")
length = 3
if int(URon) == 1:
    length = 4
out_filename = "output/"+para+".txt"

count = 0
with open(out_filename, 'w') as f:
    for line in all.readlines():
        line = line.split("\t")
        if line[0] == para:
            count += 1
            print "found matching parameter: SR #:"+str(count)
            SR = line[5]+"\t"
            for x in range(1, length):
                SR += line[x]+"\t"
            f.write(SR+"\n")
        else:
            pass
        #if count == 1230:
            #print "all SRs for this parameter have been found"
            #break

