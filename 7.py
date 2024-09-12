print('Где стоит конь?')
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

print('Куда конь пойдет?')
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

if 1 <= x1 <= 8 and 1 <= y1 <= 8:
    if 1 <= x2 <= 8 and 1 <= y2 <= 8:
        if ((x2-x1)**2+(y2-y1)**2)**0.5 % (5**0.5) == 0:
            print("Скачи скачи мой коник")
        else:
            print("Это чутка не конь")
    else:
        print("Конь выскочил за борт")
else:
    print("Поставь коняру на доску")