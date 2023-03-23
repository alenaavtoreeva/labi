import random
from random import randint
def n1():
    a = 5
    list = []
    for i in range(a):
        item = randint(1,10)
        list.append(item)
    n = int(input("Введите число: "))
    if n in list:
        print("Вы угадали число!", *list)
    else:
        print("Вы не угадали число!", *list)


def n2():
    list = [1, 2, 3, 4, 5, 5, 5, 6, ]
    c = 0
    p = 0
    for i in list:
        if list.count(i) > 1:
            c = c + 1
            p = i
    print("Число", p, "повторяется", c, "раза")


def n3():
   week = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
   d = int(input('Сколько выходных вы хотите? '))
   print('Рабочие дни: ', *week[:-d])
   print('Выходные: ', *week[-d:])


def n4():
    l1 = ['Автореева', 'Аймалетдинова', 'Иванов', 'Баданина', 'Васильева', 'Тоцкая', 'Шишкин', 'Мерзлякова', 'Жук', 'Леоненко']
    l2 = ['Сергеев', 'Худяков', 'Пегова', 'Карпов', 'Воробьёва', 'Фролов', 'Пупкин', 'Жижкин', 'Морозова', 'Котов']
    team = tuple(random.sample(l1, 2) + random.sample(l2, 2))
    print(*sorted(l1))
    print(*sorted(l2))
    print(*team)
    print(len(team))
    team = tuple(sorted(team))
    if "Иванов" in team:
        print(team).count("Иванов")
    else:
        print("Иванова нет")


n1(), n3(), n2(), n4()