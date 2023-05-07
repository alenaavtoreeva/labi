import telebot
import wikipedia
from telebot import types
import os
import random

bot = telebot.TeleBot('XXXXXXXXXXXXXXXXXXXXXXXXX')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    f = types.KeyboardButton('Поиск фильма')
    c = types.KeyboardButton('Котейку?')
    w = types.KeyboardButton('Википедия')

    markup.add(f, c, w)
    bot.send_message(message.chat.id, 'Я могу искать фильмы и сериалы на кинопоиске и скидывать рандомные картинки котиков:)', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Котейку?')
def cat(message):
    photo = open('photos/' + random.choice(os.listdir('photos')), 'rb')
    bot.send_photo(message.from_user.id, photo)
    bot.send_message(message.from_user.id, 'Также, вы можете добавить свою картинку котейки, просто скиньте её в чат')

@bot.message_handler(content_types=['photo'])
def photo_c(message):
    if message.content_type == 'photo':
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'C:/Users/111/PycharmProjects/bot1/' + file_info.file_path.replace('cats/', '')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
            bot.send_message(message.from_user.id, 'Ваше фото сохранено:)')
    else:
        pass

@bot.message_handler(func=lambda message: message.text == 'Википедия')
def get_text_messages(message):
    if message.text == 'Википедия':
        bot.send_message(message.from_user.id, 'Напиши слово и узнай его значение в википедии')
    else:
        gmessages(message)


@bot.message_handler(content_types=['text'])
def all(message):
    if message.text == 'Поиск фильма':
        bot.send_message(message.from_user.id, 'Напиши номер фильма и я скину на него ссылку в кинопоиске '
                                               '\nФильмы: \n435 - "Зелёная миля" \n326 - "Побег из Шоушенка" \n679486 - "Тайна Коко" \n476 - "Назад в будущее" \nСериалы: \n1306638 - Мир! Дружба! Жвачка! \n4647040 - Король и Шут \n4476885 - Извне \n464963 - Игра престолов')
    if message.text == '435' or message.text == '326' or message.text == '679486' or message.text == '476' or message.text == '1306638' or message.text == '4647040' or message.text == '4476885' or message.text == '464963':
        bot.send_message(message.from_user.id,
                         "https://www.kinopoisk.ru/film/" + message.text.replace(' ', '+') + '/')
    elif message.text != 'Поиск фильма':
        gmessages(message)
def gmessages(message):
    try:
        wikipedia.set_lang('ru')
        bot.send_message(message.from_user.id, wikipedia.summary(str(message.text)))
    except:
        bot.send_message(message.from_user.id, 'У слова нет точного определения')
        bot.send_message(message.from_user.id, "Можете проверить по этой ссылке: " + "https://ru.wikipedia.org/wiki/" + message.text.replace(' ', '+'))



bot.polling(none_stop=True, interval=0)

