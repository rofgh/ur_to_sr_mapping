from itertools import combinations

l1 = ["Aux", "NegP", "Adv", "O2", "PP", "O1"]
total = []
for r in range(0,len(l1)):
    l_perm = combinations(l1, r)
    for x in l_perm:
        total.append(x)
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
print(len(total))
count = 0
for x in total:
    count += 1
    print("\n"+str(count)+":\t", end="")
    print("S", end="\t")
    print("V", end="\t")
    for y in x:
        print(y, end="\t")

print()
print()