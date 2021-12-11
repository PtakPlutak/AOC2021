f = open("input.txt", "r")
inp = f.readlines()
f.close()

inp=[[int(x) for x in line.strip("\n")] for line in inp]
#inp=[[int(x) for x in line] for line in inp]
mx=len(inp[0])
my=len(inp)

#add padding
pad=9
inp2=[[pad for i in range(mx+2)] for j in range(my+2)]
for j in range(my):
    for i in range(mx):
        if inp[j][i]!=9:
            inp2[j+1][i+1]=0
inp=inp2

#recurrent check
def findbasin(y,x,val):
    inp[y][x]=val
    if inp[y-1][x]==0: findbasin(y-1,x,val)
    if inp[y+1][x]==0: findbasin(y+1,x,val)
    if inp[y][x-1]==0: findbasin(y,x-1,val)
    if inp[y][x+1]==0: findbasin(y,x+1,val)

#basins?
basins=[]
curbas=0
for y in range(1,my+1):
    for x in range(1,mx+1):
        #print(y,x,inp[y][x])
        if inp[y][x]==0:
            curbas+=-1
            findbasin(y,x,curbas)
for line in inp:
    print(line)

for i in range(-1,curbas-1,-1):
    sum=0
    for y in range(1,my+1):
        for x in range(1,mx+1):
            if inp[y][x]==i: sum+=1
    print(i, sum)
    basins.append(sum)
basins.sort()
print(basins[-1]*basins[-2]*basins[-3])

