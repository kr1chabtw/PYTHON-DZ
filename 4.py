a = int(input('Который час? '))
if 0 <= a <= 23:
    if 5 <= a <= 11:
        print('Доброе утро')
    elif 12 <= a <= 17:
        print('Пора обедать, братанчик')
    elif 18 <= a <= 22:
        print('Вечер в хату')
    else:
        print('Сладких снов')
else:
    print('Ошибка')