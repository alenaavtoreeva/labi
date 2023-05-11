def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def ice_flavors(self):
            print('Вкусы мороженого:')
            print(*self.flavors, sep='\n')

    s = IceCreamStand("Мороженка", 'кафе', ['ваниль', 'клубника', 'шоколад'])
    s.ice_flavors()

def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    class IceCreamStand(Restaurant):
        def __init__(self,restaurant_name, cuisine_type, flavors, loc, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.place = loc
            self.time = time

        def ice_flavors(self):
            print('Виды мороженного: ')
            print(*self.flavors, sep='\n')

        def newflavor(self):
            self.flavors.append(input('Введите новый сорт: '))

        def delflavor(self):
            self.flavors.remove(input('Введите сорт, который хотите удалить: '))

        def poisk(self):
            if input('Какой вкус хотите найти? ') in self.flavors:
                print('В наличии')
            else:
                print('Нет в наличии')

    class na_palochke(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, loc, time, material):
            super().__init__(restaurant_name, cuisine_type, flavors, loc, time)
            self.material = material

        def palochka(self):
            print('Материал палочки:', self.material)

    s = IceCreamStand("Морожка", 'кафе', ['ваниль', 'клубника', 'шоколад'], 'ул. Садовая', '6:00-18:00')
    s.describe_restaurant()
    s.newflavor()
    s.ice_flavors()
    s.delflavor()
    s.ice_flavors()
    s.poisk()

    g = na_palochke("Морожка", 'кафе', ['ваниль', 'клубника'], 'Вознесенский пр.', '8:00-22:00', 'дерево')
    g.palochka()

import tkinter as tk
def z3():
    class IceCreamStand:
        def __init__(self):
            self.names = ['Как раньше', 'Ekzo', 'Коровка из Кореновки', 'Свитлогорье', 'Даша', 'Золотая трубочка']
            self.types = ['Пломбир', 'Эскимо', 'Стаканчик', 'Пломбир', 'Брикет', 'Рожок']

        def get_names(self):
            return self.names

        def get_types(self):
            return self.types

    class IceCreamStandGUI:
        def __init__(self, master):
            self.master = master
            master.title("Ice Cream Stand")

            self.ice_cream_stand = IceCreamStand()
            self.names_label = tk.Label(master, text='Название', font='Calibri 12 italic bold')
            self.names_listbox = tk.Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_names()))

            for name in self.ice_cream_stand.get_names():
                self.names_listbox.insert(tk.END, name)

            self.types_label = tk.Label(master, text='Вид', font='Calibri 12 italic bold')
            self.types_listbox = tk.Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_types()))

            for type in self.ice_cream_stand.get_types():
                self.types_listbox.insert(tk.END, type)

            self.names_label.grid(row=0, column=0)
            self.names_listbox.grid(row=1, column=0)
            self.types_label.grid(row=0, column=1)
            self.types_listbox.grid(row=1, column=1)

    root = tk.Tk()
    a = IceCreamStandGUI(root)
    root.mainloop()

z3()