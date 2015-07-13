# -*- coding: utf-8 -*-

__author__ = u"Ozgur Firat Cinar"

from flask import Flask, render_template
from random import randint


app = Flask(__name__)

replies = [u'peki.', u'pekiiii', u'tamam', u'öptüm', u'görüşürüz', u'yemek masasındayım, haberleşiriz', u'aman be!',
           u'asıl sana peki.', u'kızdın mı?', u'uyuyacağım ben. iyi geceler.', u'noldu yine?']


main_text = u"Sevgilinizden gelen \"peki.\" mesajlarina vereceğiniz cevabınız yoksa,\
            butonu kullanarak cevaplar üretebilirsiniz."

@app.route('/')
def hello_world():
    cevap_text = ''
    return render_template('index.html', welcome_text=main_text, reply=cevap_text)

@app.route("/cevap/", methods=['GET'])
def cevap():
    cevap_text = generate_reply()
    return render_template('index.html', welcome_text=main_text, reply=cevap_text)

def generate_reply():
    r_number = randint(0, len(replies)-1)
    return replies[r_number]

if __name__ == '__main__':
    app.run()
