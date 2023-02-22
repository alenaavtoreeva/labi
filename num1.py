pas = input('Введите пароль: ')
pas1 = input('Повторите пароль: ')

if len(pas) < 5:
    print('Пароль слишком короткий')
if pas[0:6] == "qwerty":
    print('Пароль ненадёжный')
if pas == pas1:
     print('Пароли совпадают')
else:
     print('Пароли не совпадают')