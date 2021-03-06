#INPUT: 0001110001110 0 0
#sys.argv[1]: parameter settings in binary form, thirteen digits long: "0001110001110" 
#sys.argv[2]: do you want to see the UR treelets?
#sys.argv[3]: do you want to see the gaps?


#OUTPUT:  tab delimited text file with the parameter settings as the filename
# listing all the SR produced by the language, and the UR for each, if sys.argv[2] is on
# 
# 


import sys
from collections import defaultdict
import time

def get_one(para, out_filename, URon, gaps):
    data = open("SRs/COLAG_2011_flat.txt")
    SR_dict = defaultdict(lambda:'')
    SR_dict["header"] = ["BracketedTree #", "ILLOC Force", "SOW", "Bracketed Tree"]
    highest_line5 = 0
    count = 0
    for line in data.readlines():
        line = line.split("\t")
        #print(line[0])
        #print(para)
        if line[0] == para:
            count += 1
            #print "found matching parameter and UR #:"+line[5]
            if int(line[5]) > highest_line5:
                highest_line5 = int(line[5])
            if URon == True:
                #print "true"
                SR_dict[int(line[5])] = [line[1], line[2], line[3]]
                #print SR_dict[int(line[5])]
            if URon == False:
                #print "false"
                SR_dict[int(line[5])] = [line[1], line[2]]
                #print SR_dict[int(line[5])]
    print("\nFound "+str(count)+" SRs for this parameter")
    if count == 0:
        print("no printout required\n")
        return
    with open(out_filename, 'w') as f:
        outp = ''
        for x in SR_dict["header"]:
            outp += x+"\t"
        f.write(outp+"\n")
        if gaps == True:
            for x in range(0,highest_line5+1):
                #print SR_dict[x]
                outp = str(x)+"\t"
                for col in SR_dict[x]:
                    outp += col+"\t"
                #print outp
                f.write(outp+"\n")
        if gaps == False:
            for x in range(0,highest_line5+1):
                if len(SR_dict[x]) > 1:
                    outp = str(x)+"\t"
                    for col in SR_dict[x]:
                        outp += col+"\t"
                    #print outp
                    f.write(outp+"\n")
    print("Printed to:    "+str(out_filename)+"\n")

def get_all(URon=False, gaps=False):
    for x in range(0, 8192):
        para = str(format(x, '013b'))
        #print(para)
        out_filename = "SRs/output/"+para+".txt"
        get_one(para, out_filename, URon, gaps)



        # SR = line[5]+"\t"
        # for x in range(1, length):
        #     SR += line[x]+"\t"
        # f.write(SR+"\n")
    #if count == 1230:
        #print "all SRs for this parameter have been found"
        #break


if __name__ == '__main__':
    start = time.time()
    try:
        par = sys.argv[1]
    except:
        print("\nNo argument = at least 3072 files will be created!")
        print("And it will most likely crash your computer...")
        print("and take ~9 hours... (8-10 seconds per file)!\n")
        really = input("--Are you sure??? y/n  ")
        if really == "y":
            get_all()
            print("all done")
            exit()
        else:
            print("\nFirst argument is the list of parameter settings!\n")
            exit()
    out_filename = "SRs/output/"+par
    if len(par) != 13:
        print("\nWrong parameter settings length, it should be thirteen digits long! Try again!")
        exit()
    try:
        if int(sys.argv[2]) == 1:
            URon = True
            out_filename += "_UR"
        else:
            URon = False
    except:
        print("\nMissing Argument 2: Do you want to see the URs or not?")
        exit()
    try:
        if int(sys.argv[3]) == 1:
            gaps = True
            out_filename += "_gaps"
        else:
            gaps = False
    except:
        print("\nMissing Argument 3: Do you want to see gaps for the missing/unrealizable URs?")
        exit()
    out_filename += ".txt"
    get_one(par, out_filename, URon, gaps)
    elapsed = time.time()-start
    print("elapsed time for this grab: "+str(elapsed))