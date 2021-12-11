f = open("input.txt", "r")
inp = f.readlines()
f.close()

inp=[[int(x) for x in line.strip("\n")] for line in inp]
#inp=[[int(x) for x in line] for line in inp]
mx=len(inp[0])
my=len(inp)

#add padding
pad=10
inp2=[[pad for i in range(mx+2)] for j in range(my+2)]
for j in range(my):
    for i in range(mx):
        inp2[j+1][i+1]=inp[j][i]
inp=inp2
sum=0
for y in range(1,my+1):
    for x in range(1,mx+1):
        #print(y,x,inp[y][x])
        if inp[y][x]<inp[y][x-1] and inp[y][x]<inp[y][x+1] and inp[y][x]<inp[y-1][x] and inp[y][x]<inp[y+1][x]:
            sum=sum+inp[y][x]+1
            #print(y,x,inp[y][x])
#for line in inp:
#    print(line)
print(sum)

#inp2[:]=[[pad if i=0 or i=mx+1 or j=0 or j=my+1 else inp[j-1][i-1] for i in range(mx+2)] for j in range(my+2)]
#inp2=[[inp[y][x] for x in range(1,mx+1)] for y in range(1,my+1)]
#inp=[line.insert(0,10) for line in inp]

# sum=0
# for y in range(1,my+1):
#     for x in range(1,mx+1):
#         if inp[y][x]<inp[y][x-1] and inp[y][x]<inp[y][x+1]:
#             print(inp[y][x-1])
#             sum=sum+inp[y][x]+1