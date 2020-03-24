# -*- coding: UTF-8 –*-
# # Copyright © 2020  jinzhijie
# Open source with GPLv3 LICENSE

from flask import Flask, redirect, render_template, abort, send_from_directory
import requests
import random
import os
from cacheimg import cache, cached_json, reload_cache
app = Flask(__name__)

BASEDOMAIN = 'https://global.bing.com'


# 主页
@app.route('/')
def index():
    return render_template('index.html')


# favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', code='404 Not Found', error=error, detail='页面不见了，请检查你的 URL'), 404


@app.errorhandler(400)
def bad_request(error):
    return render_template('error.html', code='400 Bad Request', error=error, detail='请求格式有误，请参照手册发起请求'), 400


# 今日美图
@app.route('/bing')
def bing():
    req = requests.get(
        BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=-1&n=1')  # 默认第二天/今天
    pic_info = req.json()['images'][0]  # 改进写法，优化性能
    cache(pic_info, BASEDOMAIN)  # 需要在 cacheimg.py 中设置相关信息
    return redirect(BASEDOMAIN+pic_info['url'])


# 历史美图
@app.route('/bing/<int:daysago>')
def bing_daysago(daysago):
    if isinstance(daysago, int) and daysago <= 7 or daysago == -1:  # 判断是否为 int，默认 >= 0，所以只需判断是否 <= 7 即可
        req = requests.get(
            BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=%d&n=1' % int(daysago))
        pic_url = req.json()['images'][0]['url']
        return redirect(BASEDOMAIN+pic_url)
    else:
        abort(400)


# 随机美图
@app.route('/bing/random')
def bing_random():
    req = requests.get(BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=%d&n=1' %
                       random.randint(-1, 7))  # -1 ~ 7天
    pic_url = req.json()['images'][0]['url']
    return redirect(BASEDOMAIN+pic_url)


# 返回本地缓存的图片
@app.route('/bing/cache')
def bing_cache():
    img_name = cache(cached_json(BASEDOMAIN), BASEDOMAIN)  # 需要在 cacheimg.py 中设置相关信息
    return send_from_directory('caches', img_name)  # 直接返回图片，不重定向耗费时间

@app.route('/bing/cache/reload')
def bing_cache_reload():
    reload_cache()
    return 'Cache Reloaded'


if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 81)  # 可反代81端口
