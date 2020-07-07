# -*- coding: utf-8 -*-
import unittest
from Parser import Parse

class TestURL(unittest.TestCase):

    def setUp(self):
        self.Parse = Parse

    def test_url_eur(self):
        self.assertEqual(self.Parse.create_URL(self, "Евро в Уфе"), 'https://mainfin.ru/currency/eur/ufa')

    def test_url_jpy(self):
        self.assertEqual(self.Parse.create_URL(self, "Курс Йен в москве"), 'https://mainfin.ru/currency/jpy/moskva')

    def test_url_usd(self):
        self.assertEqual(self.Parse.create_URL(self, "доллары в мАхачкалЕ"), 'https://mainfin.ru/currency/usd/mahachkala')

    def test_url_gbp(self):
        self.assertEqual(self.Parse.create_URL(self, "КУРС ФУНТОВ в РОСТОВЕ"), 'https://mainfin.ru/currency/gbp/rostov-na-donu')

    def test_url_cny(self):
        self.assertEqual(self.Parse.create_URL(self, "Курс юаней в большом питере"), 'https://mainfin.ru/currency/cny/sankt-peterburg')

if __name__ == '__main__':
    unittest.main()
