from collections import defaultdict
import time

start = time.time()
data = open("SRs/COLAG_2011_flat.txt")
count = defaultdict(lambda:0)
cou = defaultdict(lambda:[])
for line in data.readlines():
    line = line.split("\t")
    if line[2] == "S Verb O1                                         ":
        count[line[0]] += 1
        cou[line[0]].append(line[3])
total = 0
with open("SVO.txt", 'w') as f:
    for x in sorted(count):
        total += count[x]
        f.write(str(x)+"\t"+str(count[x])+"\n")
        for y in cou[x]:
            f.write(""+"\t"+""+"\t"+str(y)+"\n")
print("total: "+str(total))
elapsed = time.time()-start
print("elapsed time for this grab: "+str(elapsed)+" seconds")
data.close()
