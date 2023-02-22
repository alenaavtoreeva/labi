a = int(input('Введите номер места: '))

if (a >= 36) and (a <= 54):
    if a % 2 == 0:
        print('Боковое верхнее')
    else:
        print('Боковое нижнее')
elif a % 2 == 0:
    print('Верхнее')
elif a % 2 != 0:
    print('Нижнее')