s = [3,3,5,4,5]
m = len(s)//2
if len(s)%2 != 0:
    m += 1
l = s[:m]
r = s[m:]
print([l,r])

p = []
f = (len(p)+1)//2
l = p[:f]
r = p[f:]
print([l,r])