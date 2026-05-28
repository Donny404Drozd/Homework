n = [0,1,0,0,4,3]
l = []
o = []
for e in n:
    if e == 0:
        o.append(0)
    else:
        l.append(e)
n = l + o
print(n)
