# coding: utf-8

from googletrans import Translator
from google_trans_new import google_translator  


t1 = Translator(service_urls=['translate.googleapis.com'])
t2 = google_translator()  


result = t2.translate('Urlaub')

print(result)