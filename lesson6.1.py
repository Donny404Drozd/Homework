import string

u = input("Введіть дві літери через дефіс(а-c): ")
s = u[0]
e = u[2]

a = string.ascii_letters
t = a.find(s)
n = a.find(e)
r = ""
for i in range(t, n + 1):
    r = r + a[i]
print(r)