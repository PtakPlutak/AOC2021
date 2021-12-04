f = open("input.txt", "r")
inp = f.readlines()
f.close()

nums=[int(s) for s in inp[0].split(',')]

inp.pop(0)
inp.pop(0)
#inp.remove("\n")
inp=[(el.split()) for el in inp]
inp=[[int(k) for k in line] for line in inp]

print(len(inp))
print(inp)
def foo():
    for num in nums:
        print(num)
        inp[:] = [[x if x!=num else -1 for x in line] for line in inp]
        for k in range(int((len(inp)+1)/6)):
            tmpBingo=inp[6*k:6*k+5]
            for i in range(5):
                if sum(tmpBingo[i])==-5 or sum([tmpBingo[j][i] for j in range(5)])==-5:
                    print(num)
                    tmpBingo[:] = [[x if x!=-1 else 0 for x in line] for line in tmpBingo]
                    print(num,num*sum(sum(x) for x in tmpBingo))
                    return
foo()
