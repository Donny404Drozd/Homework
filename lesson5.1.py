import keyword
import string

u = input("Введіть ім'я змінної:")
n = True
if len(u) == 0:
    n = False
if len(u) > 0:
    if u[0] in "0123456789":
        n = False
if "__" in u:
    n = False
if u in keyword.kwlist:
    n = False
for char in u:
    if char.isupper():
        n = False
    if char == " ":
        n = False
    if char in string.punctuation and char != "_":
        n = False
print(n)