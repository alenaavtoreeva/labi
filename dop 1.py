f = open("synonyms.txt")
mas = []
for line in f:
    line = str(line)
    p = ''.join(line.split())
    mas.append(p)
print("Введите ваше слово с большой буквы")
c = str(input())
l = len(c)
k = 0

for sl in mas:
    if sl.find(c, 0, l) != -1:
        ll = len(sl)
        syn = sl[l+1:ll]
        print(syn)
        k = 1

if k == 0:
    print("Такого слова нет в словаре")

print("Синоним верный?(да/нет)")
otv = str(input())
if otv == 'да':
    print("Отлично")
if otv == 'нет':
    print("Введите свой вариант: ")
    var = str(input())
    with open("synonyms.txt", "a") as file:
        file.write(c + "-" + var + '\n')
        file.close()
    print("Слово добавлено в словарь")
