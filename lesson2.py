import math
from statistics import mean

print ('Квадрат числа')
d=int(input('Введіть число?'))
g=(d**2)
print('Результат:',g)
print('  ')

d=pow(int(input('Введіть число?')),2)
print('Результат:',d)
print('  ')


print ('Середнє трьох чисел')

a=int(input('Перше число?'))
n=int(input('Друге число?'))
f=int(input('Третє число?'))
g=(a+n+f)/3
print('Результат:',g)
print('  ')


print('Перетворення хвилин у години')
w=int(input('Введіть кількість хвилин:'))
v = (w//60)
c = (w%60)
print('Результат:',v,"годин",':',c,"хвилин")
print('  ')

print('Перетворення годин у хвилини')
w=int(input('Введіть кількість годин'))
v = (w*60)
f = (v*60)
print('Результат:',v,"хвилин",f,"секунд")
print('  ')

print('Розрахунок знижки')
d=int(input('Введіть ціну:'))
f=int(input('Введіть знижку(%):'))
g=(d-(d/100*f))
t=(d/100*f)
print('Сума знижки:',t)
print('Ціна зі знижкою:',g)
print('  ')

print('Остання цифра числа')
t=int(input('Введіть число:'))
print('Результат:',t%10)
print('  ')

print('Остання цифра числа')
t=input('Введіть число:')
print(t[-1])
print('  ')

print('Периметр прямокутника')

d=float(input('Ввеіть довжину:'))
f=float(input('Введіть ширину:'))
print('Результат:',(2*(d+f)))
print('  ')

print('Виведення числа в стовпчик')
print('  ')
m=int(input("Введіть число:"))
q,r=divmod(m,1000)
print(q)
q,r=divmod(r,100)
print(q)
q,r=divmod(r,10)
print(q)
print(r)
print('  ')
print('Виведення числа в стовпчик')

w=int(input('Введіть число:'))
v = (w//1000)
c = (w%1000)
g = (c//100)
f = (c%100)
b = (f//10)
a = (f%10)

print(v)
print(g)
print(b)
print(a)
print('  ')

print('Виведення числа в стовпчик')
w=input('Введіть число:')
print((w[0]),(w[1]),(w[2]),(w[3]),sep='\n')

