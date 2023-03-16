def n1(number):
    try:
        if number % 3 == 0:
            return True
        else:
            return False
    except ValueError:
        print('Это не число!')

def n2(number):
    b = None
    try:
        b = 100 / float(number)
    except ValueError:
        print('Это не число!')
    except ZeroDivisionError:
        print('Вы ввели ноль')
    else:
        print(f'Результат: {b}')
    return b

def n3(date):
    try:
        date = date.split('.')
        if int(date[0]) * int(date[1]) == int(date[2][2:4]):
            return True
        else:
            return False
    except:
        print('Дата введена в неправильном формате!')

def n4(bil):
    x = 0
    y = 0
    if len(bil) % 2 == 0:
        for i in bil[0:int(len(bil) / 2)]:
            x = x + int(i)
        for i in bil[int(len(bil) / 2):int(len(bil))+1]:
            y = y + int(i)
        if x == y:
            return True
        else:
            return False
    else:
        print('Количество цифр нечётно!')

if __name__ == "__main__":
    print('Проверка функции деления на три:')
    print(n1(2))
    print(n1(9))

    print('\nПроверка функции деления 100 на число:')
    print(n2(100))
    print(n2(0))
    print(n2('aaa'))

    print('\nПроверка функции магической даты:')
    print(n3('11.02.2022'))
    print(n3('12.01.2022'))
    print(n3('12.01.22'))

    print('\nПроверка функции счастливого билета:')
    print(n4('123456'))
    print(n4('001100'))