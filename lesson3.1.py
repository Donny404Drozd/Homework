
try:
    n = float(input("Введіть перше число: "))
    o = input("Яку дію необхідно виконати (+, -, *, /): ")
    m = float(input("Введіть друге число: "))
    if o == '+':
        r = n + m
    elif o == '-':
        r = n - m
    elif o == '*':
        r = n * m
    elif o == '/':
        if m != 0:
            r = n / m
        else:
            r = "Ну шо ти робиш??"
    else:
        r = "Стає погано від твоїх дій"
    print("Результат:", r)

except ValueError:
    print("Помилка: Будь ласка, вводьте тільки числа!")



m=[12, 3, 4, 10, 8]
if m:
    n = m.pop()
    m.insert(0, n)
print(m)

m = [0,3,4,6,78,78,5]
if len(m) > 0:
    m.insert(0, m.pop())
print(m)

m = [9,3,4,5,6,2]
m.insert(0, m.pop()) if m else None
print(m)


s = [1, 2, 3, 4, 5]

m = len(s) // 2
if len(s) % 2 != 0:
    m += 1
l = s [:m]
r = s [m:]
print([l,r])

p = [5,6,6,7,8,8,8,8]
f = (len(p)+1) // 2
l = p[:f]
r = p[f:]
print([l,r])


