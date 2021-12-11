f = open("input.txt", "r")
inp = f.readlines()
f.close()

# () {} <> []
td = {
")": "(",
"}": "{",
">": "<",
"]": "[",
}

tp = {
")": 3,
"]": 57,
"}": 1197,
">": 25137,
}
score=0
for line in inp:
    tmp=[line[0]]
    for x in line[1:]: #append and pop
        if x in "({<[" or x=="\n":
            #print(x)
            tmp.append(x)
        else:
            if td[x]==tmp[-1]:
                tmp.pop(-1)
            else:
                print("ERROR:",tmp, x, tp[x])
                score=score+tp[x]
                break
print(score)