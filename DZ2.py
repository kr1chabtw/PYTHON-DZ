# Задача 2
# Напишите программу, которая предлагает ввести два целых числа и выясняет,
# делится ли первое число на второе без остатка (кратно ли второе число).
# Предусмотрите вариант, когда в качестве второго числа можно ввести 0
# (на ноль же делить нельзя). В этом случае программа ничего вычисляет,
# а просто завершает выполнение.
a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

if b != 0:
    if a % b != 0:
        print('Не делится без остатка')
    elif a % b == 0:
        print(f'Делимое : Делитель = {a/b}')