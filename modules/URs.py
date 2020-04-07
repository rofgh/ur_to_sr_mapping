from itertools import combinations

# Writes a .txt containing all possible Question URs
def all_QURS():
    l1 = [" Aux", " NegP", " Adv", " O1", " O2", " PP"]
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
    # for x in total:
    #     print(x)
    #     if "O2" in x:
    #         if "O1" not in x:
    #             total.remove(x)
    #             print("deleted"+str(x))
    #             continue

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
    base = [" Verb", " S"]
    for UR in total:
        for x in base:
            UR.insert(0, x) 

    #print(len(total))
    count   = 0
    objs = [" S", " Adv", " O1", " O2", " PP"]
    no_top = total.copy()
    for UR in no_top:
        for obj in objs:
            topUR = []
            if obj in UR:
                topUR = UR.copy()
                ind     = topUR.index(obj)
                topUR.insert(ind, obj+"+t")
                topUR.remove(obj)
                total.append(topUR)

    whs = [" S", " Adv", " O1", " O2", " PP", " S+t", " Adv+t", " O1+t", " O2+t", " PP+t"]
    no_Q = total.copy()
    for UR in no_Q:
        for wh in whs:
            whUR = []
            if wh in UR:
                whUR = UR.copy()
                ind     = whUR.index(wh)
                whUR.insert(ind, wh+"+wh")
                whUR.remove(wh)
                total.append(whUR)
            
    # Uncomment for printing the numbers   
    # for x in total:
    #     count += 1
    #     print("\n"+str(count)+":\t", end="")
    #     #print("S", end="\t")
    #     #print("V", end="\t")
    #     for y in x:
    #         print(y, end="\t")

    with open("UR_writer/all_QURs.txt", 'w') as f:
        for UR in total:
            for item in UR:
                f.write(str(item)+"\t")
            f.write("\n")

# Writes a .txt containing all possible Declarative URs
def all_DURS():
    l1 = [" Aux", " NegP", " Adv", " O1", " O2", " PP"]
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
    # for x in total:
    #     print(x)
    #     if "O2" in x:
    #         if "O1" not in x:
    #             total.remove(x)
    #             print("deleted"+str(x))
    #             continue

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
    base = [" Verb", " S"]
    for UR in total:
        for x in base:
            UR.insert(0, x) 

    #print(len(total))
    count   = 0
    objs = [" S", " Adv", " O1", " O2", " O3", " PP"]
    no_top = total.copy()
    for UR in no_top:
        for obj in objs:
            topUR = []
            if obj in UR:
                topUR = UR.copy()
                ind     = topUR.index(obj)
                topUR.insert(ind, obj+"t")
                topUR.remove(obj)
                total.append(topUR)
            
    # Uncomment for printing the numbers   
    # for x in total:
    #     count += 1
    #     print("\n"+str(count)+":\t", end="")
    #     #print("S", end="\t")
    #     #print("V", end="\t")
    #     for y in x:
    #         print(y, end="\t")

    with open("UR_writer/all_DURs.txt", 'w') as f:
        for UR in total:
            for item in UR:
                f.write(str(item)+"\t")
            f.write("\n")


# Writes a .txt containing all possible Imperative URs
def all_IURS():
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
    # for x in total:
    #     print(x)
    #     if "O2" in x:
    #         if "O1" not in x:
    #             total.remove(x)
    #             print("deleted"+str(x))
    #             continue

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

   #print(len(total))
    
    # Uncomment for printing the numbers       
    # count = 0
    # for x in total:
    #     count += 1
    #     print("\n"+str(count)+":\t", end="")
    #     #print("S", end="\t")
    #     #print("V", end="\t")
    #     for y in x:
    #         print(y, end="\t")

    with open("UR_writer/all_IURs.txt", 'w') as f:
        for UR in total:
            for item in UR:
                f.write(str(item)+"\t")
            f.write("\n")

def all_URs():
    all_DURS()
    all_IURS()
    all_QURS()
