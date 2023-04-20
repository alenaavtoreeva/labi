from PIL import Image
from PIL import ImageFilter
import os

def n1():
    pic = 'C:/Users/111/PycharmProjects/bot/pic'
    savepic = 'C:/Users/111/PycharmProjects/bot/savepic'
    if not os.path.exists(savepic):
        os.makedirs(savepic)
    for file in os.listdir(pic):
        with Image.open(os.path.join(pic, file)) as img:
            filtpic = img.filter(ImageFilter.CONTOUR)
            filtpic.save(os.path.join(savepic, file))
def n2():
    pic = 'C:/Users/111/PycharmProjects/bot/pic1'
    savepic = 'C:/Users/111/PycharmProjects/bot/savepic'
    if not os.path.exists(savepic):
        os.makedirs(savepic)
    for file in os.listdir(pic):
        if file.endswith('.jpg') or file.endswith('.png'):
            with Image.open(os.path.join(pic, file)) as img:
                filtpic = img.filter(ImageFilter.CONTOUR)
                filtpic.save(os.path.join(savepic, file))
        else:
            print('Неверное расширение у файла ' + file)

import csv
def n3():
    with open('data.csv') as r_file:
        file_reader = csv.DictReader(r_file, delimiter= ',')
        print('Нужно купить:')
        sum = 0
        for row in file_reader:
            print(f'{row["Продукт"]} - {row["Количество"]}' + ' шт.', end='')
            print(f' за {row["Цена"]} руб.')
            sum += int(row["Цена"])
        print(f'Итоговая сумма: {sum} руб.')


n1(), n2(), n3()