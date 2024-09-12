a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print(f'Меньшее число - {b}')
elif b > a:
    print(f'Меньшее число - {a}')
else:
    print(f'Число {a} = число {b}')