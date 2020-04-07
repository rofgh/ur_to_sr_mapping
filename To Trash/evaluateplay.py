
def Parameter1(n):
    print("1")

def Parameter2(n):
    print("2")

def Parameter3(n):
    print("3")

Pa = [0,0,1,1,1,1,1,1,1,1,1,1,1]

for x in range(1,len(Pa)+1):
        func = "Parameter"+str(x)+"(Pa["+str(Pa[x])+"])"
        eval(func)

