# import telebot
# import requests
# from io import BytesIO
# import webbrowser
# from telebot import types
# import requests
# from bs4 import BeautifulSoup
# import telebot
# from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
#
# bot = telebot.TeleBot('7209705890:AAGtnFSgIGVuzs8teT-yMad0bI4PylfRgq0')
#
#
#
# def conn(message):
#     bot.send_message(message.chat.id, "номера для обратной связи \n "
#                                       "+996 707 009 522\n "
#                                       "+996 223 232 758\n ")
#
#
# def location(message):
#     bot.send_message(message.chat.id,
#                      "Купить номера или заброннировать можете на нашем сайте http://127.0.0.1:8000/api/v1/apartment/")
#
#
#
#
#
# @bot.message_handler(commands=['location'])
# def location_get(message):
#     location(message)
#
#
# @bot.message_handler(commands=['connection'])
# def connection_get(message):
#     conn(message)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'handle_start')
# def handle_go_to_tickets(call):
#     handle_start(call.message)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'location')
# def go_to_location(call):
#     location(call.message)
#
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('http://127.0.0.1:8000/api/v1/apartment/')
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'conn')
# def send_conn(call):
#     conn(call.message)
#
#
# @bot.message_handler(commands=['info'])  # Это будет выполняться для всех входящих сообщений
# def send_hello(message):
#     markup = types.InlineKeyboardMarkup(row_width=4)
#     markup.add(types.InlineKeyboardButton('Адресс', callback_data='location'))
#     markup.add(types.InlineKeyboardButton('Обратная связь', callback_data='conn'))
#     markup.add(types.InlineKeyboardButton('Прасмотр номеров', callback_data='handle_start'))
#     bot.send_message(message.chat.id, 'Приветствую', reply_markup=markup)
#
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     bot.send_message(message.chat.id, 'Вот ссылка на сайт: http://127.0.0.1:8000/api/v1/apartment/')
#
#
# @bot.message_handler(commands=['start', 'restart'])
# def start_command(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('Переход на сайт')
#     item2 = types.KeyboardButton('Просмотр номеров')
#     item3 = types.KeyboardButton('Обратная связь')
#     item4 = types.KeyboardButton('Информация')
#     item5 = types.KeyboardButton('start')
#     markup.add(item1, item2, item3, item4, item5)
#
#     sticker_id1 = 'CAACAgIAAxkBAAEMP51mYYxLlgUrBUpskVutQzJgmXhpWwACEhgAAhAemUi_BAQfVRhL4TUE'
#     bot.send_sticker(message.chat.id, sticker_id1)
#
#     bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)
#
#
# @bot.message_handler(commands=['restart'])
# def restart_bot(message):
#     bot.send_message(message.chat.id, start_command)
#
#
# @bot.message_handler(func=lambda message: message.text == 'start')
# def start_bot(message):
#     start_command(message)
#
#
# @bot.message_handler(func=lambda message: message.text == 'Переход на сайт')
# def view_website(message):
#     site(message)
#
#
# @bot.message_handler(func=lambda message: message.text == 'Просмотр номеров')
# def start(message):
#     """Отправляет сообщение при вводе команды /start."""
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(InlineKeyboardButton('Просмотр номеров', callback_data='view_apartments'))
#     bot.send_message(message.chat.id, 'Добро пожаловать! Нажмите кнопку ниже, чтобы просмотреть квартиры.', reply_markup=keyboard)
#
#
# bot = telebot.TeleBot('7209705890:AAGtnFSgIGVuzs8teT-yMad0bI4PylfRgq0')
# API_URL = 'http://127.0.0.1:8000/api/v1/apartment/'  # Замените на ваш фактический URL
#
# @bot.callback_query_handler(func=lambda call: call.data == 'view_apartments')
# def view_apartments(call):
#     """Обрабатывает нажатие кнопки 'Просмотр номеров'."""
#     response = requests.get(API_URL)
#     if response.status_code != 200:
#         bot.send_message(call.message.chat.id, "Ошибка при получении данных о квартирах.")
#         return
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#     apartments = soup.select('.apartment-card')
#
#     if not apartments:
#         message = "В данный момент нет доступных квартир."
#     else:
#         message = "Доступные квартиры:\n\n"
#         for apartment in apartments:
#             title = apartment.find('h3').text
#             location = apartment.find('p', text=lambda x: x and 'Location:' in x).text.split(': ')[1]
#             price = apartment.find('p', text=lambda x: x and 'Price:' in x).text.split(': ')[1]
#             price_dollar = apartment.find('p', text=lambda x: x and 'Price in Dollars:' in x).text.split(': ')[1]
#             description = apartment.find('p', text=lambda x: x and 'Description:' in x).text.split(': ')[1]
#             details_url = apartment.find('a')['href']
#
#             message += f"Название: {title}\n"
#             message += f"Местоположение: {location}\n"
#             message += f"Цена: {price}\n"
#             message += f"Цена в долларах: {price_dollar}\n"
#             message += f"Описание: {description}\n"
#             message += f"Подробнее: http://127.0.0.1:8000{details_url}\n\n"
#
#     bot.send_message(call.message.chat.id, message)
#
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     start(message)
#
# def main():
#     bot.polling(none_stop=True)
#
#
# @bot.message_handler(func=lambda message: message.text == 'Обратная связь')
# def conn_but(message):
#     conn(message)
#
#
# @bot.message_handler(func=lambda message: message.text == 'Информация')
# def informate(message):
#     send_hello(message)
#
#
# if __name__ == "__main__":
#     bot.polling(none_stop=True)
# #
#
#
# # Замените 'your_token' на ваш фактический токен Telegram-бота
# bot = telebot.TeleBot('7209705890:AAGtnFSgIGVuzs8teT-yMad0bI4PylfRgq0')
# API_URL = 'http://127.0.0.1:8000/api/v1/apartment/'  # Замените на ваш фактический URL
#
# @bot.callback_query_handler(func=lambda call: call.data == 'view_apartments')
# def view_apartments(call):
#     """Обрабатывает нажатие кнопки 'Просмотр номеров'."""
#     response = requests.get(API_URL)
#     if response.status_code != 200:
#         bot.send_message(call.message.chat.id, "Ошибка при получении данных о квартирах.")
#         return
#
#     soup = BeautifulSoup(response.text, 'html.parser')
#     apartments = soup.select('.apartment-card')
#
#     if not apartments:
#         message = "В данный момент нет доступных квартир."
#     else:
#         message = "Доступные квартиры:\n\n"
#         for apartment in apartments:
#             title = apartment.find('h3').text
#             location = apartment.find('p', text=lambda x: x and 'Location:' in x).text.split(': ')[1]
#             price = apartment.find('p', text=lambda x: x and 'Price:' in x).text.split(': ')[1]
#             price_dollar = apartment.find('p', text=lambda x: x and 'Price in Dollars:' in x).text.split(': ')[1]
#             description = apartment.find('p', text=lambda x: x and 'Description:' in x).text.split(': ')[1]
#             details_url = apartment.find('a')['href']
#
#             message += f"Название: {title}\n"
#             message += f"Местоположение: {location}\n"
#             message += f"Цена: {price}\n"
#             message += f"Цена в долларах: {price_dollar}\n"
#             message += f"Описание: {description}\n"
#             message += f"Подробнее: http://127.0.0.1:8000{details_url}\n\n"
#
#     bot.send_message(call.message.chat.id, message)
#
# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     start(message)
#
# def main():
#     bot.polling(none_stop=True)
#
# if __name__ == '__main__':
#     main()
#
#
#
#
#



import telebot
import requests
from io import BytesIO
import webbrowser
from telebot import types
from bs4 import BeautifulSoup
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot('7209705890:AAGtnFSgIGVuzs8teT-yMad0bI4PylfRgq0')
API_URL = 'http://127.0.0.1:8000/api/v1/apartment/'  # Замените на ваш фактический URL

def conn(message):
    bot.send_message(message.chat.id, "номера для обратной связи \n "
                                      "+996 707 009 522\n "
                                      "+996 223 232 758\n ")

def location(message):
    bot.send_message(message.chat.id,
                     "Купить номера или забронировать можете на нашем сайте http://127.0.0.1:8000/api/v1/apartment/")

@bot.message_handler(commands=['location'])
def location_get(message):
    location(message)

@bot.message_handler(commands=['connection'])
def connection_get(message):
    conn(message)

@bot.callback_query_handler(func=lambda call: call.data == 'handle_start')
def handle_go_to_tickets(call):
    handle_start(call.message)

@bot.callback_query_handler(func=lambda call: call.data == 'location')
def go_to_location(call):
    location(call.message)

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('http://127.0.0.1:8000/api/v1/apartment/')

@bot.callback_query_handler(func=lambda call: call.data == 'conn')
def send_conn(call):
    conn(call.message)

@bot.message_handler(commands=['info'])
def send_hello(message):
    markup = InlineKeyboardMarkup(row_width=4)
    markup.add(InlineKeyboardButton('Адресс', callback_data='location'))
    markup.add(InlineKeyboardButton('Обратная связь', callback_data='conn'))
    markup.add(InlineKeyboardButton('Просмотр номеров', callback_data='show_apartments'))
    bot.send_message(message.chat.id, 'Приветствую', reply_markup=markup)

@bot.message_handler(commands=['start', 'restart'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Переход на сайт')
    item2 = types.KeyboardButton('Просмотр номеров')
    markup.add(item1, item2)

    sticker_id1 = 'CAACAgIAAxkBAAEMP51mYYxLlgUrBUpskVutQzJgmXhpWwACEhgAAhAemUi_BAQfVRhL4TUE'
    bot.send_sticker(message.chat.id, sticker_id1)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['restart'])
def restart_bot(message):
    bot.send_message(message.chat.id, start_command)

@bot.message_handler(func=lambda message: message.text == 'start')
def start_bot(message):
    start_command(message)

@bot.message_handler(func=lambda message: message.text == 'Переход на сайт')
def view_website(message):
    site(message)

@bot.message_handler(func=lambda message: message.text == 'Просмотр номеров')
def start(message):
    """Отправляет сообщение при вводе команды /start."""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Просмотр номеров', callback_data='show_apartments'))
    bot.send_message(message.chat.id, 'Добро пожаловать! Нажмите кнопку ниже, чтобы просмотреть квартиры.', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'show_apartments')
def show_apartments(call):
    """Отправляет сообщение с inline-кнопкой для просмотра номеров."""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Показать доступные номера', callback_data='view_apartments'))
    bot.send_message(call.message.chat.id, 'Нажмите кнопку ниже, чтобы увидеть доступные квартиры.', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'view_apartments')
def view_apartments(call):
    """Обрабатывает нажатие кнопки 'Показать доступные номера'."""
    response = requests.get(API_URL)
    if response.status_code != 200:
        bot.send_message(call.message.chat.id, "Ошибка при получении данных о квартирах.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    apartments = soup.select('.apartment-card')

    if not apartments:
        message = "В данный момент нет доступных квартир."
    else:
        message = "Доступные квартиры:\n\n"
        for apartment in apartments:
            title = apartment.find('h3').text
            location = apartment.find('p', text=lambda x: x and 'Location:' in x).text.split(': ')[1]
            price = apartment.find('p', text=lambda x: x and 'Price:' in x).text.split(': ')[1]
            price_dollar = apartment.find('p', text=lambda x: x and 'Price in Dollars:' in x).text.split(': ')[1]
            description = apartment.find('p', text=lambda x: x and 'Description:' in x).text.split(': ')[1]
            details_url = apartment.find('a')['href']

            message += f"Название: {title}\n"
            message += f"Местоположение: {location}\n"
            message += f"Цена: {price}\n"
            message += f"Цена в долларах: {price_dollar}\n"
            message += f"Описание: {description}\n"
            message += f"Подробнее: http://127.0.0.1:8000{details_url}\n\n"

    bot.send_message(call.message.chat.id, message)

def main():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()