from telethon import TelegramClient, events
from telethon.tl.types import KeyboardButton, KeyboardButtonCallback
import random

token = '1980716029:AAGBw9fQlcZDGPZFajokfEWml-YTkf1fD1w'

bot = TelegramClient('bot', 7465073, 'fccfbedddb2a3599955982c7983d8064').start(bot_token=token)


@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):    
    keyboard = [
        [  
            KeyboardButton("1к20"), 
            KeyboardButton("1к12")
        ],
        [
            KeyboardButton("1к10"), 
            KeyboardButton("1к8")
        ],
        [
            KeyboardButton('1к6'),
            KeyboardButton("1к4")
        ]
    ]
    await event.reply('Привет, не напишешь нормальное сообщение - не любишь маму) P.s. формат - *число*к*число*', buttons=keyboard)


@bot.on(events.NewMessage)
async def echo_all(event):
    if event.text != '/start':
        msg = event.text
        ind = msg.find('к')
        if ind == -1:
            await event.reply('Пидорас, введи нормально')
        else:
            try:
                first, second = int(msg[:ind:]), int(msg[ind+1::])
            except:
                await event.reply('Пидорас, введи нормально')
            await event.reply(str(random.randint(first, first*second)))
    

bot.run_until_disconnected()