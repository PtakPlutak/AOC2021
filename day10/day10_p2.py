f = open("input.txt", "r")
inp = f.readlines()
f.close()

inp=[line.strip("\n") for line in inp]

# () {} <> []
td = {
")": "(",
"}": "{",
">": "<",
"]": "[",
}

tp = {
"(": 1,
"[": 2,
"{": 3,
"<": 4,
}

scores=[]
for line in inp:
    score=0
    tmp=[line[0]]
    noerr=0
    for x in line[1:]: #append and pop
        if x in "({<[" or x=="\n":
            #print(x)
            tmp.append(x)
        else:
            if td[x]==tmp[-1]:
                tmp.pop(-1)
            else:
                #print("ERROR:",tmp, x, tp[x])
                noerr=1
                break
    #print("here")
    if noerr==0:
        for x in tmp[::-1]:
            score=5*score+tp[x]
        scores.append(score)
scores.sort()
print(scores,len(scores))
print(scores[int((len(scores)-1)/2)])