f = open("input.txt", "r")
inp=f.readlines()
f.close()

slen=len(inp[0])-1
o2=0
co2=0
inpcp=list(inp)

#most common bit
for i in range(slen):
    buc=0
    if len(inp)>1:
        for line in inp:
            if line[i]=="1":
                buc+=1
        #decision for most
        if buc>=(len(inp)/2):
            dec="1"
        else:
            dec="0"
        #print(inp,buc,dec)
        for line in list(inp):
            if line[i]!=dec:
                inp.remove(line)

o2=int(inp[0],2)

inp=inpcp
#least common bit
for i in range(slen):
    buc=0
    if len(inp)>1:
        for line in inp:
            if line[i]=="1":
                buc+=1
        #decision for most
        if buc>=(len(inp)/2):
            dec="0"
        else:
            dec="1"
        #print(inp,buc,dec)
        for line in list(inp):
            if line[i]!=dec:
                inp.remove(line)

co2=int(inp[0],2)
        
print(o2,co2,o2*co2)

