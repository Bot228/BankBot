# -*- coding: utf-8 -*-
import time
import telebot
from Parser import Parse
from requests.exceptions import ReadTimeout

bot = telebot.TeleBot('1366234798:AAH2ZMNxBlm-2k_hWOwlWj-J0yOAa5YWhIE')
parse = Parse(bot)
'''
def send_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Условия сотрудничества')
    keyboard.row('Доставка товаров', 'Возврат/Обмен')
    keyboard.row('Варианты оплаты', 'Контакты')
    keyboard.row('Подбор размера', 'Данные для отправки')
    return keyboard
'''
def send_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    keyboard.add('Подобрать размер')
    keyboard.add('Как измерить?')
    keyboard.add('Мои размеры')
    return keyboard

def sizes(message):
    with open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8") as file:
        sz = int(file.readlines()[3])
        if (sz <= 96):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "w+", encoding="utf-8") as size:
                    size.write('Для пальто, полупальто, курток, майек, поло и свитеров:\n' + 'Размер: S\n' + 'Российский размер: 44/46\n' + '\n')
                    size.close()
        elif (sz > 96 and sz <= 101):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "w+", encoding="utf-8") as size:
                    size.write('Для пальто, полупальто, курток, майек, поло и свитеров:\n' + 'Размер: M\n' + 'Российский размер: 46/48\n' + '\n')
                    size.close()
        elif (sz > 101 and sz <= 107):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "w+", encoding="utf-8") as size:
                    size.write('Для пальто, полупальто, курток, майек, поло и свитеров:\n' + 'Размер: L\n' + 'Российский размер: 48/50\n' + '\n')
                    size.close()
        elif (sz > 107 and sz <= 112):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "w+", encoding="utf-8") as size:
                    size.write('Для пальто, полупальто, курток, майек, поло и свитеров:\n' + 'Размер: XL\n' + 'Российский размер: 50/52\n' + '\n')
                    size.close()
        elif (sz > 112 and sz <= 117):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "w+", encoding="utf-8") as size:
                    size.write('Для пальто, полупальто, курток, майек, поло и свитеров:\n' + 'Размер: XXL\n' + 'Российский размер: 52/54\n' + '\n')
                    size.close()
        else:
            with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "w+", encoding="utf-8") as size:
                size.write(
                    'У нас нет в наличии пальто таких размеров\n' + '\n')
                size.close()

        if (sz <= 90):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для костюмов и блейзеров:\n' + 'Европейский размер: 44\n' + 'Российский размер: 42\n' + '\n')
                    size.close()
        elif (sz > 90 and sz <= 94):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для костюмов и блейзеров:\n' + 'Европейский размер: 46\n' + 'Российский размер: 44\n' + '\n')
                    size.close()
        elif (sz > 94 and sz <= 98):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для костюмов и блейзеров:\n' + 'Европейский размер: 48\n' + 'Российский размер: 46\n' + '\n')
                    size.close()
        elif (sz > 98 and sz <= 102):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для костюмов и блейзеров:\n' + 'Европейский размер: 50\n' + 'Российский размер: 48\n' + '\n')
                    size.close()
        elif (sz > 102 and sz <= 106):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для костюмов и блейзеров:\n' + 'Европейский размер: 52\n' + 'Российский размер: 50\n' + '\n')
                    size.close()
        elif (sz > 106 and sz <= 110):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для костюмов и блейзеров:\n' + 'Европейский размер: 54\n' + 'Российский размер: 52\n' + '\n')
                    size.close()
        elif (sz > 110 and sz <= 114):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для костюмов и блейзеров:\n' + 'Европейский размер: 56\n' + 'Российский размер: 54\n' + '\n')
                    size.close()
        else:
            with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                size.write(
                    'У нас нет в наличии костюмов таких размеров\n' + '\n')
                size.close()

        with open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8") as file2:
            sz2 = int(file2.readlines()[1])
            if (sz <= 96) and (sz2 <= 39):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для рубашек:\n' + 'Размер: S\n' + 'Российский размер: 44/46\n' + '\n')
                    size.close()
            elif (sz >= 96 and sz <= 101) and (sz2 > 39 and sz2 <= 41):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для рубашек:\n' + 'Размер: M\n' + 'Российский размер: 46/48\n' + '\n')
                    size.close()
            elif (sz >= 101 and sz <= 107) and (sz2 > 41 and sz2 <= 43):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для рубашек:\n' + 'Размер: L\n' + 'Российский размер: 48/50\n' + '\n')
                    size.close()
            elif (sz >= 107 and sz <= 112) and (sz2 > 43 and sz2 <= 45):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для рубашек:\n' + 'Размер: XL\n' + 'Российский размер: 50/52\n' + '\n')
                    size.close()
            elif (sz >= 112 and sz <= 117) and (sz2 > 45 and sz2 <= 46):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для рубашек:\n' + 'Размер: XXL\n' + 'Российский размер: 52/54\n' + '\n')
                    size.close()
            else:
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'У нас нет в наличии рубашек таких размеров\n' + '\n')
                    size.close()
            file2.close()
        file.close()
    with open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8") as file:
        sz = int(file.readlines()[5])
        if (sz <= 72):
            with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                size.write('Для брюк в спортивном стиле, спортивых костюмов, шорт и нижнего белья:\n' + 'Размер: XS\n' + 'Российский размер: 42/44\n' + '\n')
                size.close()
        elif (sz > 72 and sz <= 78):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для брюк в спортивном стиле, спортивых костюмов, шорт и нижнего белья:\n' + 'Размер: S\n' + 'Российский размер: 44/46\n' + '\n')
                    size.close()
        elif (sz > 78 and sz <= 84):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для брюк в спортивном стиле, спортивых костюмов, шорт и нижнего белья: \n' + 'Размер: M\n' + 'Российский размер: 46/48\n' + '\n')
                    size.close()
        elif (sz > 84 and sz <= 90):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для брюк в спортивном стиле, спортивых костюмов, шорт и нижнего белья:\n' + 'Размер: L\n' + 'Российский размер: 48/50\n' + '\n')
                    size.close()
        elif (sz > 90 and sz <= 96):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для брюк в спортивном стиле, спортивых костюмов, шорт и нижнего белья:\n' + 'Размер: XL\n' + 'Российский размер: 50/52\n' + '\n')
                    size.close()
        elif (sz > 96 and sz <= 102):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                    size.write('Для брюк в спортивном стиле, спортивых костюмов, шорт и нижнего белья:\n' + 'Размер: XXL\n' + 'Российский размер: 52/54\n' + '\n')
                    size.close()
        else:
            with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a", encoding="utf-8") as size:
                size.write(
                    'У нас нет в наличии брюк таких размеров\n' + '\n')
                size.close()
        with open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r+", encoding="utf-8") as file2:
            sz2 = int(file2.readlines()[7])
            if (sz <= 73 and sz2 <= 92):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для джинс и костюмных брюк:\n' + 'Европейский размер: 36\n' + 'Российский размер: 42\n' + '\n')
                    size.close()
            elif (sz >= 73 and sz <= 77) and (sz2 > 92 and sz2 <= 96):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для джинс и костюмных брюк:\n' + 'Европейский размер: 38\n' + 'Российский размер: 44\n' + '\n')
                    size.close()
            elif (sz >= 77 and sz <= 81) and (sz2 > 96 and sz2 <= 100):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для джинс и костюмных брюк:\n' + 'Европейский размер: 40\n' + 'Российский размер: 46\n' + '\n')
                    size.close()
            elif (sz >= 81 and sz <= 85) and (sz2 > 100 and sz2 <= 104):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для джинс и костюмных брюк:\n' + 'Европейский размер: 42\n' + 'Российский размер: 48\n' + '\n')
                    size.close()
            elif (sz >= 85 and sz <= 89) and (sz2 > 104 and sz2 <= 108):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для джинс и костюмных брюк:\n' + 'Европейский размер: 44\n' + 'Российский размер: 50\n' + '\n')
                    size.close()
            elif (sz >= 89 and sz <= 93) and (sz2 > 108 and sz2 <= 112):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для джинс и костюмных брюк:\n' + 'Европейский размер: 46\n' + 'Российский размер: 52\n' + '\n')
                    size.close()
            elif (sz >= 93 and sz <= 97) and (sz2 > 112 and sz2 <= 116):
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'Для джинс и костюмных брюк:\n' + 'Европейский размер: 48\n' + 'Российский размер: 54\n' + '\n')
                    size.close()
            else:
                with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "a",
                          encoding="utf-8") as size:
                    size.write(
                        'У нас нет в наличии джинс таких размеров\n' + '\n')
                    size.close()


    file.close()
    with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "r+", encoding="utf-8") as size:
        bot.send_message(message.chat.id, size.read())
        size.close()
def send_size(message):
    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '1'):
            bot.send_message(message.chat.id, 'Напишите свой обхват шеи в сантиметрах')
            bot.send_message(message.chat.id, 'Пример: 40')
            return

    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '2'):
            bot.send_message(message.chat.id, 'Напишите свой обхват груди в сантиметрах')
            bot.send_message(message.chat.id, 'Пример: 100')
            return

    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '3'):
            bot.send_message(message.chat.id, 'Напишите свой обхват талии в сантиметрах')
            bot.send_message(message.chat.id, 'Пример: 80')
            return

    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '4'):
            bot.send_message(message.chat.id, 'Напишите свой обхват бедер в сантиметрах')
            bot.send_message(message.chat.id, 'Пример: 110')
            return

    with (open(str('storage\\user_state\\' + str(message.from_user.id) + '_state.txt'), "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '5'):
            with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "r", encoding="utf-8")) as file:
                bot.send_message(message.chat.id, 'Проверьте правильность введенных размеров')
                bot.send_message(message.chat.id, file.read())
                file.close()
                keyboard2 = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
                keyboard2.add('Да', 'Нет')
                bot.send_message(message.chat.id, 'Данные верны?', reply_markup=keyboard2)
            return

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "w+", encoding="utf-8")) as state:
        state.seek(0)
        state.truncate()
        state.write('0')
    keyboard = send_keyboard()
    bot.send_message(message.chat.id, 'Привет! \nЯ тестовый бот магазина одежды TM LIMITED! \nЯ могу расчитать тебе '
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
    if (a == 'Как измерить?'):
        img = 'https://static.zara.net/static//common/images/size-guide/size-guide-man-ru_RU.png?1604642811000'
        bot.send_photo(message.chat.id, img, reply_markup=keyboard)
    if (a == 'Мои размеры'):
        try:
            file2 = open('storage\\user_ans\\' + str(message.from_user.id) + '_ans.txt', "r", encoding="utf-8")
            bot.send_message(message.chat.id, file2.read(), reply_markup=keyboard)
            file2.close()
            with open('storage\\user_size\\' + str(message.from_user.id) + '_size.txt', "r+", encoding="utf-8") as size:
                bot.send_message(message.chat.id, size.read())
                size.close()
        except:
            bot.send_message(message.chat.id, 'У вас пока нет размеров, необходимо заполнить форму', reply_markup=keyboard)
    if (a == 'Подобрать размер'):
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
                file.write('Обхват шеи:\n' + str(message.text) + '\n')
                file.close()
            state.seek(0)
            state.truncate()
            state.write('2')
            state.close()
            send_size(message)
            return

    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '2'):
            with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                file.write('Обхват груди:\n' + str(message.text) + '\n')
                file.close()
            state.seek(0)
            state.truncate()
            state.write('3')
            state.close()
            send_size(message)
            return

    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '3'):
            with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                file.write('Обхват талии:\n' + str(message.text) + '\n')
                file.close()
            state.seek(0)
            state.truncate()
            state.write('4')
            state.close()
            send_size(message)
            return

    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '4'):
            with (open('storage\\user_info\\' + str(message.from_user.id) + '.txt', "a", encoding="utf-8")) as file:
                file.write('Обхват бедер:\n' + str(message.text) + '\n')
                file.close()
            state.seek(0)
            state.truncate()
            state.write('5')
            state.close()
            send_size(message)
            return

    with (open('storage\\user_state\\' + str(message.from_user.id) + '_state.txt', "r+", encoding="utf-8")) as state:
        if (state.readline(1) == '5'):
            if (str(message.text) == 'Да'):
                bot.send_message(message.chat.id, 'Вы успешно прошли регистрацию!')
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
            elif (str(message.text) == 'Нет'):
                state.seek(0)
                state.truncate()
                state.write('1')
                state.close()
                bot.send_message(message.chat.id, 'Давайте пройдем регистрацию заново')
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


