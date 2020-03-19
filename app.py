from flask import Flask, redirect
import requests
import random
app = Flask(__name__)

BASEDOMAIN = 'https://global.bing.com'


@app.route('/bing')
def bing():
    req = requests.get(BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=-1&n=1')  # 默认第二天/今天
    pic_url = req.json()['images'][0]['url']
    return redirect(BASEDOMAIN+pic_url)


@app.route('/bing/<daysago>')
def bing_daysago(daysago):
    req = requests.get(BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=%d&n=1' % int(daysago))
    pic_url = req.json()['images'][0]['url']
    return redirect(BASEDOMAIN+pic_url)

@app.route('/bing/random')
def bing_random():
    req = requests.get(BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=%d&n=1' % random.randint(-1,7))  # -1 ~ 7天
    pic_url = req.json()['images'][0]['url']
    return redirect(BASEDOMAIN+pic_url)


if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 81)
