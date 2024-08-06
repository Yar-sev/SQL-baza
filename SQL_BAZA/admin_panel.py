import telebot
from telebot import types
from main_SQL import *

bot = telebot.TeleBot("6701177381:AAHOyJu-MZ2j8djqTT5rZlqiGIlJMOt0mA0")
def buttons_panel(user):
    if user == "admin":
        btn1 = types.KeyboardButton("профиль")
        btn2 = types.KeyboardButton("магазин")
        return btn1, btn2
    elif user == 'user':
        btn1 = types.KeyboardButton("профиль")
        btn2 = types.KeyboardButton("магазин")
        btn3 = types.KeyboardButton("панель администратора")
        return btn1, btn2, btn3
@bot.message_handler(commands=["start"])
def start(message):
    user_database(message.chat.id, message.from_user.first_name)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(buttons_panel(select_data(message.chat.id)))
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}!".format(
                         message.from_user), reply_markup=markup)

bot.infinity_polling()