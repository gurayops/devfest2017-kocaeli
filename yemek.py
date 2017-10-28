#-*-coding:utf-8-*-
import falcon
import random
import os
import time

waitTime = int(os.environ.get('WAIT_TIME', '2'))

menu = {
	u'Mercimek Çorbası': 5,
	u'Sucuklu Yumurta': 9,
	u'Omlet': 6,
	u'Akdeniz Salatası': 9,
	u'Tavuklu Salata': 12,
	u'Köri Soslu Tavuk': 16,
	u'Pirinç Pilavı': 3,
	u'Yaprak Sarma': 8,
	u'Biber Dolması': 8,
	u'Kuru Fasülye': 5,
	u'Künefe': 3,
	u'Kadayıf': 5,
	u'Penne Arabiata Makarna': 18,
	u'Kumru': 5,
	u'Pepperoni Pizza': 29,
	u'Ayvalık Tostu': 6,
	u'Adana': 7,
	u'Piliç Izgara': 15,
	u'Jetlag Buster': 23,
	u'Kavurma': 11 ,
	u'Ciğer': 9
	}

class YemekMenusu(object):
    def on_get(self, request, response):
        time.sleep(waitTime)
        response.media = menu


api = falcon.API()
api.add_route('/', YemekMenusu())

