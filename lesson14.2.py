class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        # Встановлюємо нове максимальне значення
        self.max_value = max_max

    def set_min(self, min_min):
        # Встановлюємо нове мінімальне значення
        self.min_value = min_min

    def step_up(self):
        # Якщо поточне значення вже досягло максимуму, крок вгору робити не можна
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current += 1

    def step_down(self):
        # Якщо поточне значення вже досягло мінімуму, крок вниз робити не можна
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current -= 1

    def get_current(self):
        return self.current


# --- Перевірка роботи та твої юніт-тести ---

counter = Counter()
counter.set_current(7)
counter.step_up()  # 8
counter.step_up()  # 9
counter.step_up()  # 10

assert counter.get_current() == 10, "Test1"

try:
    counter.step_up()  # Тут значення 10, тому викличеться ValueError
except ValueError as e:
    print(e)  # Виведе: Досягнуто максимуму

assert counter.get_current() == 10, "Test2"

counter.set_min(7)  # Міняємо мінімальну межу на 7
counter.step_down()  # 9
counter.step_down()  # 8
counter.step_down()  # 7

assert counter.get_current() == 7, "Test3"

try:
    counter.step_down()  # Тут значення 7, що дорівнює мінімуму -> ValueError
except ValueError as e:
    print(e)  # Виведе: Досягнуто мінімуму

assert counter.get_current() == 7, "Test4"

print("Усі тести пройдено! ОК")

