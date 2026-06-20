
s = int(input("Введіть кількість секунд: "))

d = s // 86400
se = s % 86400
h = se // 3600
se = se % 3600
m = se // 60
sec = se % 60

if 11 <= d % 100 <= 14:
    y = "днів"
elif d % 10 == 1:
    y = "день"
elif d % 10 == 2 or d % 10 == 3 or d % 10 == 4:
    y = "дні"
else:
    y = "днів"

hours = str(h).zfill(2)
minutes = str(m).zfill(2)
seconds= str(sec).zfill(2)

r = str(d) + " " + y + ", " + hours + ":" + minutes + ":" + seconds
print(r)