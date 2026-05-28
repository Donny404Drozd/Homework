n = [0,0]
if len(n) == 0:
    r = 0
else:
    s = 0
    for i in range(len(n)):
        if i % 2 == 0:
            s = s + n[i]
    l= len(n) - 1
    e = n[l]
    r = s * e
print(r)
