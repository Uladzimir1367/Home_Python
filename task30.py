# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a n = a 1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
k = int(input('Введите количество элементов: '))
list = []
for n in range(1,k+1):
    list.append(a1 + d*(n - 1))
print(list)