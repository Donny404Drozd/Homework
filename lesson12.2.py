from inspect import isgenerator


def generate_cube_numbers(end):
    num = 2  # Починаємо з числа 2 за умовою
    while True:
        cube = num**3  # Рахуємо куб поточного числа

        if cube > end:
            return  # Якщо куб перевищив межу, виходимо з генератора

        yield cube  # Якщо все ок, видаємо куб і ставимо функцію на паузу
        num += 1  # Переходимо до наступного числа


# --- Твої тести для перевірки ---
gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, "Test0"
assert list(generate_cube_numbers(10)) == [8], "оскільки воно менше 10."
assert list(generate_cube_numbers(100)) == [
    8,
    27,
    64,
], "5 у кубі це 125, а воно вже більше 100"
assert list(generate_cube_numbers(1000)) == [
    8,
    27,
    64,
    125,
    216,
    343,
    512,
    729,
    1000,
], "10 у кубі це 1000"

print("OK")
