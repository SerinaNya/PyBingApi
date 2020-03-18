from flask import Flask, redirect
import requests
app = Flask(__name__)


@app.route('/bing')
def bing():
    BASEDOMAIN = 'https://global.bing.com'
    req = requests.get(BASEDOMAIN+'/HPImageArchive.aspx?format=js&n=1')
    pic_url = req.json()['images'][0]['url']
    print(pic_url)
    return redirect(BASEDOMAIN+pic_url)


if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 80)
