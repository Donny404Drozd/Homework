
try:
    l = float(input("Введіть перше число: "))
    o = input("Яку дію необхідно виконати(+, -, *, /): ")
    m = float(input("Введіть друге число: "))
    if o == '+':
        r = l + m
    elif o == '-':
        r = l - m
    elif o == '*':
        r = l * m
    elif o == '/':
        if m != 0:
            r = l / m
        else:
            r = "Ну шо ти робиш??"
    else:
        r = "Стає погано від твоїх дій"
    print("Результат:", r)

except ValueError:
    print("Помилка: Будь ласка, вводьте тільки числа!")