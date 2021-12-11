f = open("input.txt", "r")
inp = f.readlines()
f.close()

inp=[[int(x) for x in line.strip("\n")] for line in inp]
mx=len(inp[0])
my=len(inp)

#add padding
pad=-10000000
inp2=[[pad for i in range(mx+2)] for j in range(my+2)]
for j in range(my):
    for i in range(mx):
        inp2[j+1][i+1]=inp[j][i]
inp=inp2
flashsum=0

#recursive function
def updflash(y,x):
    inp[y][x]=0
    global flashsum
    flashsum+=1
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if inp[y+j][x+i]!=0: inp[y+j][x+i]+=1
            if inp[y+j][x+i]>9: updflash(y+j,x+i)
    #print(y,x)

#main loop
for i in range(10000):
    inp=[[x+1 for x in line] for line in inp]
    #print("Before flashing: ",i+1)
    #for line in inp:
    #    print(line)
    for y in range(1,my+1):
        for x in range(1,mx+1):
            if inp[y][x]>9: updflash(y,x)
    sumP=0
    for y in range(1,my+1):
        for x in range(1,mx+1):
            sumP+=inp[y][x]
    if sumP==0:
        print(i+1)
        break
    #print("After flashing: ",i+1)
    #for line in inp:
        #print(line)

#print(flashsum)