import telebot


token = '1904656129:AAEq2rE_RSt0zfYfk2uRjsBjwMd2VthpCUA'


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.infinity_polling()