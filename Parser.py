# -*- coding: utf-8 -*-
import requests
from telebot import TeleBot
from bs4 import BeautifulSoup
from telebot.types import Message

class Parse:

    def __init__(self, bot: TeleBot):
        self.ans = ''
        self.bot = bot
        self.flag2 = False
        self.HEADERS = {'user_agent': 'head'}
        self.URL = 'https://mainfin.ru/currency/'

    def create_URL(self, message: Message):
        self.ans = ''
        self.flag2 = False
        self.URL = 'https://mainfin.ru/currency/'
        a = message.text
        a = str(a)
        a = a.lower()
        if (a != ""):
            if (a.find("доллар") != -1 or a.find("usd") != -1 or a.find("долар") != -1):
                self.URL = self.URL + 'usd/'
                self.ans = "Курс доллара в "
            elif (a.find("евро") != -1 or a.find("eur") != -1):
                self.URL = self.URL + 'eur/'
                self.ans = "Курс евро в "
            elif (a.find("юан") != -1 or a.find("cny") != -1):
                self.URL = self.URL + 'cny/'
                self.ans = "Курс юаня в "
            elif (a.find("фунт") != -1 or a.find("gbp") != -1):
                self.URL = self.URL + 'gbp/'
                self.ans = "Курс фунта в "
            elif (a.find("йен") != -1 or a.find("jpy") != -1):
                self.URL = self.URL + 'jpy/'
                self.ans = "Курс йены в "
            else:
                self.bot.send_message(message.chat.id, "Не понял запрос")
                self.flag2 = True
            if (a.find("петербург") != -1 or a.find("питер") != -1 or a.find("спб") != -1):
                self.URL = self.URL + 'sankt-peterburg'
                self.ans = self.ans + "Санкт-Петербурге"
            elif (a.find("москв") != -1):
                self.URL = self.URL + 'moskva'
                self.ans = self.ans + "Москве"
            elif (a.find("ростов") != -1):
                self.URL = self.URL + 'rostov-na-donu'
                self.ans = self.ans + "Ростове-на-Дону"
            elif (a.find("екатеринбург") != -1):
                self.URL = self.URL + 'ekaterinburg'
                self.ans = self.ans + "Екатеринбурге"
            elif (a.find("казан") != -1):
                self.URL = self.URL + 'kazan'
                self.ans = self.ans + "Казани"
            elif ((a.find("нижн") != -1 and a.find("новгород") != -1)):
                self.URL = self.URL + 'nizhniy-novgorod'
                self.ans = self.ans + "Нижнем Новгороде"
            elif (a.find("новосиб") != -1):
                self.URL = self.URL + 'novosibirsk'
                self.ans = self.ans + "Новосибирске"
            elif (a.find("омск") != -1):
                self.URL = self.URL + 'omsk'
                self.ans = self.ans + "Омске"
            elif (a.find("самар") != -1):
                self.URL = self.URL + 'samara'
                self.ans = self.ans + "Самаре"
            elif (a.find("челябинск") != -1):
                self.URL = self.URL + 'chelyabinsk'
                self.ans = self.ans + "Челябинске"
            elif (a.find("уф") != -1):
                self.URL = self.URL + 'ufa'
                self.ans = self.ans + "Уфе"
            elif (a.find("красноярск") != -1):
                self.URL = self.URL + 'krasnoyarsk'
                self.ans = self.ans + "Красноярске"
            elif (a.find("перм") != -1):
                self.URL = self.URL + 'perm'
                self.ans = self.ans + "Перми"
            elif (a.find("воронеж") != -1):
                self.URL = self.URL + 'voronezh'
                self.ans = self.ans + "Воронеже"
            elif (a.find("Волгоград") != -1):
                self.URL = self.URL + 'volgograd'
                self.ans = self.ans + "Волгограде"
            elif (a.find("краснодар") != -1):
                self.URL = self.URL + 'krasnodar'
                self.ans = self.ans + "Краснодаре"
            elif (a.find("саратов") != -1):
                self.URL = self.URL + 'saratov'
                self.ans = self.ans + "Саратове"
            elif (a.find("тюмен") != -1):
                self.URL = self.URL + 'tumen'
                self.ans = self.ans + "Тюмени"
            elif (a.find("тольят") != -1):
                self.URL = self.URL + 'tolyatti'
                self.ans = self.ans + "Тольятти"
            elif (a.find("ижевск") != -1):
                self.URL = self.URL + 'izhevsk'
                self.ans = self.ans + "Ижевске"
            elif (a.find("барнаул") != -1):
                self.URL = self.URL + 'barnaul'
                self.ans = self.ans + "Барнауле"
            elif (a.find("иркутск") != -1):
                self.URL = self.URL + 'irkutsk'
                self.ans = self.ans + "Иркутске"
            elif (a.find("ульяновск") != -1):
                self.URL = self.URL + 'ulyanovsk'
                self.ans = self.ans + "Ульяновске"
            elif (a.find("хабаровск") != -1):
                self.URL = self.URL + 'habarovsk'
                self.ans = self.ans + "Хабаровске"
            elif (a.find("ярославл") != -1):
                self.URL = self.URL + 'yaroslavl'
                self.ans = self.ans + "Ярославле"
            elif (a.find("владивосток") != -1):
                self.URL = self.URL + 'vladivostok'
                self.ans = self.ans + "Владивостоке"
            elif (a.find("махачкал") != -1):
                self.URL = self.URL + 'mahachkala'
                self.ans = self.ans + "Махачкале"
            elif (a.find("томск") != -1):
                self.URL = self.URL + 'tomsk'
                self.ans = self.ans + "Томске"
            elif (a.find("оренбург") != -1):
                self.URL = self.URL + 'orenburg'
                self.ans = self.ans + "Оренбурге"
            elif (a.find("кемерово") != -1):
                self.URL = self.URL + 'kemerovo'
                self.ans = self.ans + "Кемерово"
            elif (a.find("новокузнецк") != -1):
                self.URL = self.URL + 'novokuzneck'
                self.ans = self.ans + "Новокузнецке"
            else:
                self.ans = self.ans + "России"
            return self.URL

    def web_parse(self, message: Message):
        URL = Parse.create_URL(self, message)
        if (self.flag2 == False):
            try:
                response = requests.get(URL)
                response.encoding = 'utf8'
                soup = BeautifulSoup(response.text, 'html.parser')
                file = open(str(message.from_user.id) + '.txt', "w", encoding="utf-8")
                file.write("🌍" + self.ans + '\n' + '\n')
                for i in range(5):
                    for tag in soup.find_all('a', {"class": "currpos-{0}".format(i)}):
                        file.write("🏛" + "{0}".format(tag.text) + '\n')
                    d = soup.find('tr', {"data-key": "{0}".format(i)})
                    flag = True
                    for tag in d.findAllNext('span', {"class": "float-convert__btn"}, limit=2):
                        if (flag):
                            file.write("Покупка - {0} руб.".format(tag.text) + '\n')
                            flag = False
                        else:
                            file.write("Продажа - {0} руб.".format(tag.text) + '\n' + '\n')
                file.close()
                file = open(str(message.from_user.id) + '.txt', "r", encoding="utf-8")
                self.bot.send_message(message.from_user.id, file.read())
                file.close()
            except:
                file = open(str(message.from_user.id) + '.txt', "r", encoding="utf-8")
                self.bot.send_message(message.from_user.id, file.read())
                file.close()
                return False
