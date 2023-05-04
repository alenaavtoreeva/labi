import json

def n1():
    with open('10.json', encoding='utf8') as f:
        s = json.load(f)
    print(s)
    for i in range(len(s.get('products'))):
        k = s.get('products')[i]
        print('Название: ' + str(k.get('name')))
        print('Цена: ' + str(k.get('price')))
        if str(k.get('available')):
            print('В наличии')
        else:
            print('Нет в наличии')
        print('Вес: ' + str(k.get('weight')))

    s['products'].append({
        'name': input('Название: '),
        'price': input('Цена: '),
        'available': input('Наличие: '),
        'weight': input('Вес: ')
    })
    with open('10.json', 'w', encoding='utf8') as file:
        json.dump(s, file, indent=4, ensure_ascii=False)

def n3():
    er = open('en-ru.txt ', encoding='utf8').read().split('\n')
    s = {}
    for i in range(len(er)):
        er[i] = er[i].split(' - ')
        s[er[i][0]] = er[i][1:]
    print(s)

    s1 = {}
    for i in s:
        for k in s[i]:
            k = k.split(', ')
            for j in k:
                if j not in s1:
                    s1[j] = i
                else:
                    s1[j] = s1[j] + ', ' + i
    s1 = dict(sorted(s1.items()))
    print(s1)

    s2 = ''
    for i in s1:
        s2 += i + ' - ' + s1[i] + '\n'

    x = open('ru-en.txt', 'w+', encoding='utf8')
    x.write(s2)


n3()