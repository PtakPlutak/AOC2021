f = open("input.txt", "r")
inp = f.readlines()
f.close()

letters=[x for x in "abcdefg"]
finsum=0
for line in inp:
    [digits,output]=line.strip("\n").split(" | ")
    digits=digits.split()
    digits=["".join(sorted(x)) for x in digits]
    output=output.split()
    output=["".join(sorted(x)) for x in output]
    letterstats={}
    for x in letters:
        sumL=0
        for l in digits:
            if x in l: sumL+=1
        letterstats[sumL]=x
    digitsstats={}
    for x in digits:
        digitsstats[len(x)]=x
    letdict={} #a:b, b:d, e:g ...
    #find b, e, f, g
    letdict["b"]=letterstats[6]
    letdict["e"]=letterstats[4]
    letdict["f"]=letterstats[9]
    
    numdict={} #0: be, 1: abc ...
    #find 1, 4, 7, 8
    numdict[1]=digitsstats[2]
    numdict[4]=digitsstats[4]
    numdict[7]=digitsstats[3]
    numdict[8]=digitsstats[7]
    
    #next steps
    letdict["a"]=[x for x in numdict[7] if x not in numdict[4]][0]
    for x in letters:
        sumL=0
        for l in digits:
            if x in l: sumL+=1
        if sumL==8 and x!=letdict["a"]: letdict["c"]=x
    letdict["d"]=numdict[4].replace(letdict["b"],"").replace(letdict["c"],"").replace(letdict["f"],"")
    findg="abcdefg"
    for i in [x for x in "abcdef"]:
        findg=findg.replace(letdict[i],"")
    letdict["g"]=findg
    
    #find remaining numbers
    #0: abcefg
    tmp=""
    for i in [x for x in "abcefg"]:
        tmp=tmp+letdict[i]
    numdict[0]="".join(sorted(tmp))
    #2: acdeg
    tmp=""
    for i in [x for x in "acdeg"]:
        tmp=tmp+letdict[i]
    numdict[2]="".join(sorted(tmp))
    #3: abcefg
    tmp=""
    for i in [x for x in "acdfg"]:
        tmp=tmp+letdict[i]
    numdict[3]="".join(sorted(tmp))
    #5: abdfg
    tmp=""
    for i in [x for x in "abdfg"]:
        tmp=tmp+letdict[i]
    numdict[5]="".join(sorted(tmp))
    #6: abdefg
    tmp=""
    for i in [x for x in "abdefg"]:
        tmp=tmp+letdict[i]
    numdict[6]="".join(sorted(tmp))
    #9: abcdfg
    tmp=""
    for i in [x for x in "abcdfg"]:
        tmp=tmp+letdict[i]
    numdict[9]="".join(sorted(tmp))
    
    #reverse numdict
    tcidmun = {v: k for k, v in numdict.items()}
    
    #finally get number from output
    out=1000*tcidmun[output[0]]+100*tcidmun[output[1]]+10*tcidmun[output[2]]+tcidmun[output[3]]
    finsum+=out
    print(out)
print(finsum)