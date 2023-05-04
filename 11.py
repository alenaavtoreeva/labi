def n1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name}, Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто')

    new_restaurant = Restaurant('Ёби-Доёби', 'Азиатская')
    print(new_restaurant.restaurant_name)
    print(new_restaurant.cuisine_type)

    new_restaurant.describe_restaurant()
    new_restaurant.open_restaurant()

def n2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name}, Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто')

    r = input('Введите название ресторана: ')
    c = input('Введите тип кухни: ')

    r1 = input('Введите название ресторана: ')
    c1 = input('Введите тип кухни: ')

    r2 = input('Введите название ресторана: ')
    c2 = input('Введите тип кухни: ')

    new_restaurant1 = Restaurant(r, c)
    new_restaurant2 = Restaurant(r1, c1)
    new_restaurant3 = Restaurant(r2, c2)
    new_restaurant1.describe_restaurant()
    new_restaurant2.describe_restaurant()
    new_restaurant3.describe_restaurant()

def n3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, reiting):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.reiting = reiting

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто!')

        def write_reiting(self):
            print(fr'Бывший рейтинг: {self.reiting}')
            self.reiting = input('Обновлённое значение: ')
            print(fr'Обновлено: {self.reiting}')


    newRestaurant = Restaurant('Ёби-Доёби', 'Азиатская', '5')
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.write_reiting()

n3()