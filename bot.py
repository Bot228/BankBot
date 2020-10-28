# -*- coding: utf-8 -*-
import time
import telebot
import logging
from Parser import Parse
from requests.exceptions import ReadTimeout

logging.basicConfig(filename='history.log', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

bot = telebot.TeleBot('1366234798:AAEi6A7k7FVeume-m3Ifilq7Q-ALlotAjlc')
parse = Parse(bot)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    open(str(message.from_user.id) + '.txt', "w", encoding="utf-8")
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Каталог товаров', 'Распродажа', 'Хит продаж', 'Оплата', 'Доставка', 'Почему я могу доверять?', 'Мне не отвечают?', 'Оптовое и франчайзинговое сотрудничество')
    bot.send_message(message.chat.id, 'Привет! \nЯ тестовый бот магазина одежды TM LIMITED!', reply_markup=keyboard)


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
    #parse.web_parse(message)
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Каталог товаров', 'Распродажа', 'Хит продаж', 'Оплата', 'Доставка', 'Почему я могу доверять?',
                 'Мне не отвечают?', 'Оптовое и франчайзинговое сотрудничество')
    a = message.text
    a = str(a)
    if (a == 'Каталог товаров'):
        file = open('katalog.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    if (a == 'Распродажа'):
        file = open('ras.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    if (a == 'Хит продаж'):
        file = open('hit.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    if (a == 'Оплата'):
        file = open('buy.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    if (a == 'Доставка'):
        file = open('delivery.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    if (a == 'Почему я могу доверять?'):
        file = open('poch.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    if (a == 'Мне не отвечают?'):
        file = open('ans.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    if (a == 'Оптовое и франчайзинговое сотрудничество'):
        file = open('opt.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)

while True:
    try:
        bot.polling(none_stop=True)

    except ReadTimeout:
        time.sleep(15)
        logging.exception("Read Timeout!")

    except ConnectionError:
        time.sleep(15)
        logging.exception("Connection Error!")


