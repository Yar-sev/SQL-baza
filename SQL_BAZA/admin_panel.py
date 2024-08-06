import telebot
from telebot import types
from main_SQL import *

bot = telebot.TeleBot("6701177381:AAHOyJu-MZ2j8djqTT5rZlqiGIlJMOt0mA0")


@bot.message_handler(commands=["start"])
def start(message):
    user_database(message.chat.id, message.from_user.first_name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user = (select_data(message.chat.id)[0][3])
    if user == "user":
        btn1 = types.KeyboardButton("профиль")
        btn2 = types.KeyboardButton("магазин")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}!".format(
                         message.from_user), reply_markup=markup)
    elif user == 'admin':
        btn1 = types.KeyboardButton("профиль")
        btn2 = types.KeyboardButton("магазин")
        btn3 = types.KeyboardButton("панель администратора")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}!".format(
                         message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def message_handler(message):
    if message.text.lower() == "профиль":
        text = f"""пользователь по счёту - {select_data(message.chat.id)[0][1]}
счёт - {select_data(message.chat.id)[0][2]} Квантокоинов
имя - {select_data(message.chat.id)[0][4]}"""
        bot.send_message(message.chat.id, text)

bot.infinity_polling()