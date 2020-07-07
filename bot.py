# -*- coding: utf-8 -*-
import time
import telebot
import logging
from Parser import Parse
from requests.exceptions import ReadTimeout

logging.basicConfig(filename='history.log', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

bot = telebot.TeleBot('1391169462:AAFvQKGlYKgcBbBEF7azdpEXBglfIs4arLM')
parse = Parse(bot)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! \nНапиши запрос чтобы узнать курс валют на сегодня. \nПример : Курс доллара в Москве")

@bot.message_handler(content_types=['photo'])
def sends_photo(message):
    bot.send_message(message.chat.id, "Четкая фотка. Лучше узнай на сколько сегодня упал рубль.")

@bot.message_handler(content_types=['audio'])
def sends_photo(message):
    bot.send_message(message.chat.id, "Четкое аудио. Лучше узнай на сколько сегодня упал рубль.")

@bot.message_handler(content_types=["sticker"])
def sends_sticker(message):
    bot.send_message(message.chat.id, "Четкий стикер. Лучше узнай на сколько сегодня упал рубль.")

@bot.message_handler(content_types=['text'])
def sends_text(message):
    parse.web_parse(message)

while True:
    try:
        bot.polling(none_stop=True)

    except ReadTimeout:
        time.sleep(15)
        logging.exception("Read Timeout!")

    except ConnectionError:
        time.sleep(15)
        logging.exception("Connection Error!")


