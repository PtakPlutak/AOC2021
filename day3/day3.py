f = open("input.txt", "r")
inp=f.readlines()
f.close()

llen=len(inp)

slen=len(inp[0])-1
buc=[0]*slen

for line in inp:
    for i in range(slen):
        if line[i]=="1":
            buc[i]+=1

gm=""
ep=""
for x in buc:
    if x>(llen/2):
        gm=gm+"1"
        ep=ep+"0"
    else:
        gm=gm+"0"
        ep=ep+"1"
        
GM=int(gm,2)
EP=int(ep,2)
        
print(GM*EP)
