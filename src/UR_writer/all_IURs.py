from itertools import combinations

l1 = [" NegP", " Adv", " O1", " O2", " PP"]
total = []
for r in range(0,len(l1)+1):
    l_perm = combinations(l1, r)
    for UR in l_perm:
        l = []
        for item in UR:
            l.append(item)
        total.append(l)


'''
print(len(total))
for x in total:
    if "S" not in x:
        total.remove(x)
        print("deleted"+str(x))
        continue
'''
for x in total:
    print(x)
    if "O2" in x:
        if "O1" not in x:
            total.remove(x)
            print("deleted"+str(x))
            continue

####If we want to print a difference between NOT/NEVER:
# negs = [" not", " never"]
# negatives = total.copy()
# for UR in negatives:
#     if " NegP" in UR:
#         total.remove(UR)
#         for neg in negs:
#             negUR   = []
#             negUR   = UR.copy()
#             ind     = negUR.index(" NegP")
#             negUR.insert(ind, neg)
#             negUR.remove(" NegP")
#             total.append(negUR)
base = [" Verb"]
for UR in total:
    for x in base:
        UR.insert(0, x) 

print(len(total))
           
count = 0
for x in total:
    count += 1
    print("\n"+str(count)+":\t", end="")
    #print("S", end="\t")
    #print("V", end="\t")
    for y in x:
        print(y, end="\t")

with open("all_IURs.txt", 'w') as f:
    for UR in total:
        for item in UR:
            f.write(str(item)+"\t")
        f.write("\n")





print()
print()