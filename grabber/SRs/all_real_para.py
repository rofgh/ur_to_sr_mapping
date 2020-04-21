all =  open("COLAG_2011_flat.txt")
p_list = []
for line in all.readlines():
    line = line.split("\t")
    if line[0] not in p_list:
        p_list.append(line[0])
p_list.sort()
with open("all_real_p.txt", 'w') as f:
    for x in p_list:
        f.write(x+"\n")
print("\noutput file: all_real_p.txt with "+str(len(p_list))+" languages\n")

