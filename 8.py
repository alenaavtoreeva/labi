from PIL import Image

def n1():
    im = Image.open('dr.jpg')
    im_c = im.crop((50, 150, 700, 700))
    im_c.save('crdr.jpg')
    im_c.show()

def n2():
    otkr = {'день рождения': 'dr.jpg', '8 марта': '8m.jpg', '23 февраля': '23а.jpg'}
    h = input('Праздник: ')
    if h in otkr:
        z = otkr[h]
        g = Image.open(z)
        g.show()

from PIL import ImageFont
from PIL import ImageDraw

def n3():
    img = Image.open("postcard.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial_bold.ttf", 30)
    name = input('Введите имя получателя: ')
    draw.text((130, 30), name, (255, 255, 255), font=font)
    img.save('named.postcard.jpg')
    img.show()


n1(), n2(), n3()