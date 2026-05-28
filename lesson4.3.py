import random
l = random.randint(3,10)
f = []
for i in range(l):
    r = random.randint(1,100)
    f.append(r)
s = [f[0],f[2],f[-2]]
print(f,"==",s)