# -*- coding: utf-8 -*-
import time
import telebot
from Parser import Parse
from requests.exceptions import ReadTimeout

bot = telebot.TeleBot('1366234798:AAH2ZMNxBlm-2k_hWOwlWj-J0yOAa5YWhIE')
parse = Parse(bot)
matrix = \
[[0,155,160,165,170,175,180,185,190,195,200,205,210,215,220,225,230,235],
[50,1,1,1,1,1,1,2,2,2,2,3,3,3,4,4,4,5],
[55,1,1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5],
[60,1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5],
[65,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,5],
[70,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,5,5],
[75,1,2,2,2,2,3,3,3,4,4,4,5,5,5,5,5,5],
[80,2,2,2,2,3,3,3,4,4,4,5,5,5,5,5,5,5],
[85,2,2,2,3,3,3,4,4,4,5,5,5,5,5,5,5,5],
[90,2,2,3,3,3,4,4,4,5,5,5,5,5,5,5,5,5],
[95,2,3,3,3,4,4,4,5,5,5,5,5,5,5,5,5,5],
[100,3,3,3,4,4,4,5,5,5,5,5,5,5,5,5,5,5],
[105,3,3,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5],
[110,3,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5],
[115,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
[120,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
[125,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
[130,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]]

'''
def send_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Условия сотрудничества')
    keyboard.row('Доставка товаров', 'Возврат/Обмен')
    keyboard.row('Варианты оплаты', 'Контакты')
    keyboard.row('Подбор размера', 'Данные для отправки')
    return keyboard
'''
def create_tuple(a, b):
    return a, b

def send_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Узнать размер 📏')
    keyboard.add('Мои размеры 👕')
    return keyboard

def sizes(message):
    with open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8") as file:
        hg = float(file.readlines()[1])
        with open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8") as file2:
            wg = float(file2.readlines()[3])
            with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "w+", encoding="utf-8") as size:
                file3 = open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8")
                fit = file3.readlines()[5]
                if hg % 5 != 0:
                    hg += 5
                    hg -= (hg % 5)
                if wg % 5 != 0:
                    wg += 5
                    wg -= (wg % 5)
                hg = int(hg)
                wg = int(wg)
                a = [0, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235]
                c = [0, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130]
                b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
                x = dict(zip(a, b))
                y = dict(zip(c, b))
                if (hg <= 155):
                    mysize = 'Ваш размер одежды: XS'
                elif (wg <= 50):
                    mysize = 'Ваш размер одежды: XS'
                elif (hg >= 225):
                    mysize = 'Ваш размер одежды: XS'
                elif (wg >= 130):
                    mysize = 'Ваш размер одежды: XS'
                elif (matrix[x[hg]][y[wg]] == 1):
                    if (fit == 'Slim Fit 👚'):
                        mysize = 'Ваш размер одежды: XS'
                    elif (fit == 'Regular Fit 👔'):
                        mysize = 'Ваш размер одежды: S'
                elif (matrix[x[hg]][y[wg]] == 2):
                    if (fit == 'Slim Fit 👚'):
                        mysize = 'Ваш размер одежды: S'
                    elif (fit == 'Regular Fit 👔'):
                        mysize = 'Ваш размер одежды: M'
                elif (matrix[x[hg]][y[wg]] == 3):
                    if (fit == 'Slim Fit 👚'):
                        mysize = 'Ваш размер одежды: M'
                    elif (fit == 'Regular Fit 👔'):
                        mysize = 'Ваш размер одежды: L'
                elif (matrix[x[hg]][y[wg]] == 4):
                    if (fit == 'Slim Fit 👚'):
                        mysize = 'Ваш размер одежды: L'
                    elif (fit == 'Regular Fit 👔'):
                        mysize = 'Ваш размер одежды: XL'
                elif (matrix[x[hg]][y[wg]] == 5):
                    if (fit == 'Slim Fit 👚'):
                        mysize = 'Ваш размер одежды: XL'
                    elif (fit == 'Regular Fit 👔'):
                        mysize = 'Ваш размер одежды: XXL'
                bot.send_message(message.chat.id, mysize)
                size.write(mysize)
                size.close()
                file3.close()
                file2.close()
                file.close()

def send_size(message):
    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '1'):
            bot.send_message(message.chat.id, 'Напишите свой рост в сантиметрах')
            bot.send_message(message.chat.id, 'Пример: 180')
            return

    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '2'):
            bot.send_message(message.chat.id, 'Напишите свой вес в килограммах')
            bot.send_message(message.chat.id, 'Пример: 70')
            return

    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '3'):
            keyboard2 = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
            keyboard2.add('Slim Fit 👚', 'Regular Fit 👔')
            text = 'Какой размер предпочитаете?\nЕсли вам нравится приталенная одежда, то выберите Slim Fit ' \
                   '\nЕсли вам нравится более свободная одежда, то выберите Regular Fit'
            bot.send_message(message.chat.id, text, reply_markup=keyboard2)
            return

    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '4'):
            with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "r", encoding="utf-8")) as file:
                bot.send_message(message.chat.id, 'Проверьте правильность введенных данных')
                bot.send_message(message.chat.id, file.read())
                file.close()
                keyboard2 = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                keyboard2.add('Да 👍', 'Нет 👎')
                bot.send_message(message.chat.id, 'Данные верны?', reply_markup=keyboard2)
            return

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "w+", encoding="utf-8")) as state:
        state.seek(0)
        state.truncate()
        state.write('0')
    keyboard = send_keyboard()
    bot.send_message(message.chat.id, 'Привет! \nЯ калькулятор размеров by Begmenov! \nЯ могу расчитать тебе '
                                      'размер одежды!', reply_markup=keyboard)

'''
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
'''
@bot.message_handler(content_types=['photo'])
def sends_photo(message):
    bot.send_message(message.chat.id, "Крутая фотография")

@bot.message_handler(content_types=['audio'])
def sends_photo(message):
    bot.send_message(message.chat.id, "Крутое аудио")

@bot.message_handler(content_types=["sticker"])
def sends_sticker(message):
    bot.send_message(message.chat.id, "Крутой стикер")
'''
@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id, 'Ваши контактные данные 👇')
    with (open(str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8")) as file:
        bot.send_message(message.chat.id, file.read())
        file.close()
    keyboard = send_keyboard()
    bot.send_message(message.chat.id, 'Вы вернулись в основное меню!', reply_markup=keyboard)
'''
@bot.message_handler(content_types=['text'])
def sends_text(message):
    keyboard = send_keyboard()
    a = message.text
    a = str(a)
    if (a == 'Мои размеры 👕'):
        try:
            file2 = open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r", encoding="utf-8")
            bot.send_message(message.chat.id, file2.read(), reply_markup=keyboard)
            file2.close()
            with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "r+", encoding="utf-8") as size:
                bot.send_message(message.chat.id, size.read())
                size.close()
        except:
            bot.send_message(message.chat.id, 'У вас пока нет размеров, необходимо заполнить форму', reply_markup=keyboard)
    if (a == 'Узнать размер 📏'):
        with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
            if (state.readline(1) == '0'):
                state.seek(0)
                state.truncate()
                state.write('1')
                state.close()
                send_size(message)
                return
    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '1'):
            with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "w+", encoding="utf-8")) as file:
                try:
                    float(message.text)
                    file.write('Ваш рост:\n' + str(message.text) + '\n')
                    file.close()
                    state.seek(0)
                    state.truncate()
                    state.write('2')
                    state.close()
                    send_size(message)
                except:
                    bot.send_message(message.chat.id, 'Вы ввели неправильные символы!')
            return

    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '2'):
            with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                try:
                    float(message.text)
                    file.write('Ваш вес:\n' + str(message.text) + '\n')
                    file.close()
                    state.seek(0)
                    state.truncate()
                    state.write('3')
                    state.close()
                    send_size(message)
                except:
                    bot.send_message(message.chat.id, 'Вы ввели неправильные символы!')

    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '3'):
            if (str(message.text) == 'Slim Fit 👚'):
                #bot.send_message(message.chat.id, 'Ваши данные успешно записаны!')
                with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                    file.write('Ваш крой:\n' + str(message.text))
                    file.close()
                state.seek(0)
                state.truncate()
                state.write('4')
                state.close()
                send_size(message)
                #keyboard = send_keyboard()
                #bot.send_message(message.chat.id, 'Вы вернулись в основное меню!', reply_markup=keyboard)
                return
            elif (str(message.text) == 'Regular Fit 👔'):
                with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                    file.write('Ваш крой:\n' + str(message.text))
                    file.close()
                state.seek(0)
                state.truncate()
                state.write('4')
                state.close()
                send_size(message)
                #bot.send_message(message.chat.id, 'Давайте заполним форму заново')
                #send_size(message)
                return

    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '4'):
            if (str(message.text) == 'Да 👍'):
                bot.send_message(message.chat.id, 'Ваши данные успешно записаны!')
                file = open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "r+", encoding="utf-8")
                file2 = open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "w", encoding="utf-8")
                file2.write(file.read())
                file2.close()
                file.close()
                state.seek(0)
                state.truncate()
                state.write('0')
                state.close()
                sizes(message)
                keyboard = send_keyboard()
                bot.send_message(message.chat.id, 'Вы вернулись в основное меню!', reply_markup=keyboard)
                return
            elif (str(message.text) == 'Нет 👎'):
                state.seek(0)
                state.truncate()
                state.write('1')
                state.close()
                bot.send_message(message.chat.id, 'Давайте заполним форму заново')
                send_size(message)
                return

    '''
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
    '''
while True:
    try:
        bot.polling(none_stop=True)

    except ReadTimeout:
        time.sleep(15)

    except ConnectionError:
        time.sleep(15)


