def n2():
    slovo = input('Введите слово: ')
    s = ''
    while slovo != 'stop':
        s += slovo + ' '
        slovo = input('Введите слово: ')
    print(s)

def n3():
    slovo = input('Введите слово: ')
    while slovo != 'stop':
        if 'Ф' in slovo or 'ф' in slovo:
            print('Ого! Это редкое слово!')
        else:
           print('Эх, это не очень редкое слово...')
        slovo = input('Введите слово: ')

def n4():
    from random import randint
    print('Для завершения игры введите слово stop')
    p = 0
    np = 0
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f'{a} + {b} = ', end='')
        res = input()
        while not res.isdigit() and res != "stop":
            print('Вы ввели что-то не то, повторите ввод: ', end='')
            res = input()
        if res == 'stop':
            break
        res = int(res)
        if a + b == res:
            print('Правильно!')
            p = p + 1
        else:
            print('Неправильно!')
            np = np + 1
        if np == 3:
            print('Игра окончена, правильных ответов: ', p)
            break

print(n2(), n3(), n4())