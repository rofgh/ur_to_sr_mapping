from collections import defaultdict
import time

start = time.time()
data = open("SRs/COLAG_2011_flat.txt")
count = defaultdict(lambda:defaultdict(lambda:0))
SRs = []
for line in data.readlines():
    line = line.split("\t")
    count[line[4]][line[0]] += 1
most_for_a_lang = 0
most_for_a_sentence = 0
sent = None
sent_lang = None
for x in sorted(count):
    c = 0
    #print("sentence"+str(x), end='is used:  ')
    #print(len(count[x]), end=" languages use th sentence: ")
    total = 0
    for y in sorted(count[x]):
        total += count[x][y]
        if most_for_a_lang < count[x][y]:
            most_for_a_lang = count[x][y]
            sent_lang = (x, y)
    #print(total)
    up = int(x)
    if most_for_a_sentence < total:
        most_for_a_sentence = total
        sent = x
    print("sentence "+str(up)+" is used "+str(total)+" times over "+str(len(count[x]))+" languages")
print("the most usages for one lang: "+str(most_for_a_lang)+" by sentence: "+str(sent_lang[0])+" in lang: "+str(sent_lang[1]))
print("the most usages across all langs: "+str(most_for_a_sentence)+" by sentence: "+str(sent)+": \"S Verb Aux\"")


print("# of sentences: ", end="")
print(len(count))
elapsed = time.time()-start
print("elapsed time for this grab: "+str(elapsed)+" seconds")
data.close()
