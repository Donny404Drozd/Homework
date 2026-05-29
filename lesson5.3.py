import string

u=input("Введіть текст для хештегу: ")
t = u.title()
h = "#"
for c in t:
    if c != " " and c not in string.punctuation:
        h = h + c
if len(h) > 140:
    h = h[0:140]
print(h)
