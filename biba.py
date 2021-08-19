import telebot
import json
from telebot import types

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
def get_results():
    global db
    text =  f"Результат\n ЦТТ Spark : {list(db.values()).count(1)}\n ЦТТ Полет Мысли :{list(db.values()).count(2)}\n ЦТТ  АртТех {list(db.values()).count(3)}"
    return text
db = {}
token = '1981878407:AAHq7VSsqSPr0nqEZFMw_SHiu98G4IPUaJw'
print(get_results())
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def Reply(message): # Название функции не играет никакой роли
    global db
    if message.text == "/start":
        markup = types.ReplyKeyboardMarkup()
        buttonA = types.KeyboardButton('ЦТТ Spark')
        buttonB = types.KeyboardButton('ЦТТ Полет Мысли')
        buttonC = types.KeyboardButton('ЦТТ АртТех')
        buttonD = types.KeyboardButton('Результаты')

        markup.row(buttonA, buttonB,    buttonC)
        markup.row(buttonD)
        bot.send_message(message.chat.id, "Выбери название:ЦТТ Spark, ЦТТ Полет Мысли, ЦТТ АртТех?", reply_markup=markup)
    elif message.text == "ЦТТ Spark":
        if message.from_user.id in db:
            bot.send_message(message.chat.id, "Ваш голос поменялся на ЦТТ Spark")
            db[message.from_user.id] = 1
            bot.send_message(message.chat.id, get_results())
        else:
            db[message.from_user.id] = 1
            bot.send_message(message.chat.id, "Спасибо за ваш голос!")
            bot.send_message(message.chat.id, get_results())
    elif message.text == "ЦТТ Полет Мысли":
        if message.from_user.id in db:
            bot.send_message(message.chat.id, "Ваш голос поменялся на ЦТТ Полет Мысли")
            db[message.from_user.id] = 2
            bot.send_message(message.chat.id, get_results())
        else:
            db[message.from_user.id] = 2
            bot.send_message(message.chat.id, "Спасибо за ваш голос!")
            bot.send_message(message.chat.id, get_results())
    elif message.text == "ЦТТ  АртТех":
        if message.from_user.id in db:
            bot.send_message(message.chat.id, "Ваш голос поменялся на ЦТТ АртТех")
            db[message.from_user.id] = 3
            bot.send_message(message.chat.id, get_results())
        else:
            db[message.from_user.id] = 3
            bot.send_message(message.chat.id, "Спасибо за ваш голос!")
            bot.send_message(message.chat.id, get_results())
    elif message.text == "Результаты":
        bot.send_message(message.chat.id, get_results()) 
    else:
        bot.send_message(message.chat.id, "Выбери название:ЦТТ Spark, ЦТТ Полет Мысли, ЦТТ  АртТех?")

if __name__ == '__main__':
    bot.infinity_polling()