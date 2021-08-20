import telebot
from telebot import types
from pymongo import MongoClient
from pprint import pprint




client = MongoClient("mongodb+srv://Biba_buba_13:Vgfgh4335RTF@huyaster.bi6ms.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)


TOKEN = '1872015987:AAH634kkfiHKelxTgFdulySC-RXyBBVRMr8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hel(message):
    if db.tele.find({'id': message.from_user.id}).count()==0:
        bot.send_message(message.from_user.id, "Hi, what's your name?")
        bot.register_next_step_handler(message, get_name)
    else:
        name =  db.tele.find({'id': message.from_user.id})[0]['name']
        bot.send_message(message.from_user.id, f"Hello back {name}")



def get_name(message): #получаем фамилию
    name = message.text
    if name.lower() == "матвей" or name.lower() == "matvey":
        bot.send_message(message.from_user.id, "Не пиши мне пидор")
    else:
        user = {
            'id':message.from_user.id,
            'name':name
        }
        result=db.tele.insert_one(user)
        bot.send_message(message.from_user.id, "What's your surname?")
        bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    #fivestarcount = db.reviews.find({'id': message.from_user.id}).count()
    #print(fivestarcount)
    surname = message.text
    result = db.tele.update_one({'id' : message.from_user.id}, {'$set': {'surname': surname}})
    bot.send_message(message.from_user.id, "Спасибо!")

    
"""@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)"""


bot.polling()