# -*- coding: utf-8 -*-
import time
import telebot
from Parser import Parse
from requests.exceptions import ReadTimeout

bot = telebot.TeleBot('1366234798:AAEi6A7k7FVeume-m3Ifilq7Q-ALlotAjlc')
parse = Parse(bot)

def send_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Условия сотрудничества')
    keyboard.row('Доставка товаров', 'Возврат/Обмен')
    keyboard.row('Варианты оплаты', 'Контакты')
    keyboard.row('Подбор размера', 'Данные для отправки')
    return keyboard

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    with (open(str(message.from_user.id) + '_state.txt', "w+", encoding="utf-8")) as state:
        state.seek(0)
        state.truncate()
        state.write('0')
    keyboard = send_keyboard()
    bot.send_message(message.chat.id, 'Привет! \nЯ тестовый бот магазина одежды TM LIMITED!', reply_markup=keyboard)

@bot.message_handler(commands=['reg'])
def reg_guest(message):
    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '0'):
            state.seek(0)
            state.truncate()
            state.write('1')
            bot.send_message(message.chat.id, 'Для регистрации тебе необходимо прислать нам свою контактную информацию')
            bot.send_message(message.chat.id, 'Напиши свое ФИО через пробел 👇')
            bot.send_message(message.chat.id, 'Пример: Иванов Иван Иванович')
            state.close()

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '2'):
            bot.send_message(message.chat.id, 'Напиши свой адрес через запятую 👇')
            bot.send_message(message.chat.id, 'Пример: Россия, Москва, Тверская, 1')
            state.close()

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '3'):
            bot.send_message(message.chat.id, 'Напиши свой почтовый индекс 👇')
            bot.send_message(message.chat.id, 'Пример: 140014')
            state.close()

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '4'):
            bot.send_message(message.chat.id, 'Напиши свой телефон 👇')
            bot.send_message(message.chat.id, 'Пример: +77007007070')
            state.close()

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '5'):
            bot.send_message(message.chat.id, 'Проверь на правильность введенные данные 👇')
            file = open(str(message.from_user.id) + '.txt', "r+", encoding="utf-8")
            bot.send_message(message.chat.id, file.read())
            file.close()
            keyboard2 = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            keyboard2.add('Да', 'Нет')
            bot.send_message(message.chat.id, 'Данные верны?', reply_markup=keyboard2)
            state.close()

@bot.message_handler(content_types=['photo'])
def sends_photo(message):
    bot.send_message(message.chat.id, "Четкая фотка")

@bot.message_handler(content_types=['audio'])
def sends_photo(message):
    bot.send_message(message.chat.id, "Четкое аудио. Лучше узнай на сколько сегодня упал рубль.")

@bot.message_handler(content_types=["sticker"])
def sends_sticker(message):
    bot.send_message(message.chat.id, "Четкий стикер. Лучше узнай на сколько сегодня упал рубль.")

@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id, 'Ваши контактные данные 👇')
    with (open(str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8")) as file:
        bot.send_message(message.chat.id, file.read())
        file.close()
    keyboard = send_keyboard()
    bot.send_message(message.chat.id, 'Вы вернулись в основное меню!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def sends_text(message):
    keyboard = send_keyboard()
    a = message.text
    a = str(a)
    if (a == 'Условия сотрудничества'):
        file = open('1.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    elif (a == 'Доставка товаров'):
        file = open('2.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    elif (a == 'Возврат/Обмен'):
        file = open('3.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    elif (a == 'Варианты оплаты'):
        file = open('4.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    elif (a == 'Контакты'):
        file = open('5.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    elif (a == 'Данные для отправки'):
        file = open('6.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)
    elif (a == 'Подбор размера'):
        file = open('7.txt', "r", encoding="utf-8")
        bot.send_message(message.chat.id, file.read(), reply_markup=keyboard)

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '1'):
            with (open(str(message.from_user.id) + '.txt', "w+", encoding="utf-8")) as file:
                file.write(str(message.text)+'\n')
                file.close()
            state.seek(0)
            state.truncate()
            state.write('2')
            state.close()
            reg_guest(message)
            return

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '2'):
            with (open(str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                file.write(str(message.text)+'\n')
                file.close()
            state.seek(0)
            state.truncate()
            state.write('3')
            state.close()
            reg_guest(message)
            return

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '3'):
            with (open(str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                file.write(str(message.text)+'\n')
                file.close()
            state.seek(0)
            state.truncate()
            state.write('4')
            state.close()
            reg_guest(message)
            return

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '4'):
            with (open(str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                file.write(str(message.text)+'\n')
                file.close()
            state.seek(0)
            state.truncate()
            state.write('5')
            state.close()
            reg_guest(message)
            return

    with (open(str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '5'):
            if (str(message.text) == 'Да'):
                bot.send_message(message.chat.id, 'Вы успешно прошли регистрацию!')
                file = open(str(message.from_user.id) + '.txt', "r+", encoding="utf-8")
                file2 = open(str(message.from_user.id) + '_ans.txt', "w", encoding="utf-8")
                file2.write(file.read())
                file2.close()
                file.close()
                state.seek(0)
                state.truncate()
                state.write('0')
                state.close()
                keyboard = send_keyboard()
                bot.send_message(message.chat.id, 'Вы вернулись в основное меню!', reply_markup=keyboard)
                return
            elif (str(message.text) == 'Нет'):
                state.seek(0)
                state.truncate()
                state.write('0')
                state.close()
                bot.send_message(message.chat.id, 'Давайте пройдем регистрацию заново')
                reg_guest(message)
                return

while True:
    try:
        bot.polling(none_stop=True)

    except ReadTimeout:
        time.sleep(15)

    except ConnectionError:
        time.sleep(15)


