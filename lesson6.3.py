
n = int(input("Введіть ціле число: "))

while n > 9:
    p = 1
    for digit_char in str(n):
        p = p * int(digit_char)
    n = p
print("Результат:", n)