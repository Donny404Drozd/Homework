m=[12,3,4,10,8]
if m:
    n = m.pop()
    m.insert(0, n)
print(m)

m = [0,3,4,6,78,5]
if len(m) > 0:
    m.insert(0, m.pop())
print(m)

m = [9,3,4,5,6,2]
m.insert(0, m.pop()) if m else None
print(m)