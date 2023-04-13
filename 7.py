from PIL import Image

def n1():

    filename = 'sobaken.jpg'
    with Image.open(filename) as img:
        img.load()

    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print('Ширина: ', width)
    print('Высота: ', height)
    print('Формат: ', format)
    print('Цветовая модель: ', mode)


from PIL import ImageOps
def n2():
    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()
    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("resized_sobaken.jpg")
    new_img = img.rotate(90)
    new_img.save("rotated_sobaken.jpg")
    new_img = ImageOps.mirror(img)
    new_img.save('MirSobaken.jpg')


from PIL import ImageFilter
def n3():
    for i in range(1,6):
        im = Image.open(str(i) + '.jpg')
        im = im.filter(ImageFilter.CONTOUR)
        im.save('changed.' + str(i) + '.jpg')
        im.show()


def n4():
    i = Image.open('watermark.png')
    f = Image.open('2.jpg')
    f.paste(i, (100,100), i)
    f.save('2watermarked.jpg')
    f.show()


n1(), n2(), n3(), n4()