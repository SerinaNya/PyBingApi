import os
import requests
import time

AUTOCACHE = True
CACHEDJSON = {}


def cache(json_info, BASEDOMAIN):
    if AUTOCACHE:
        url = json_info['url']
        hsh = json_info['hsh']
        img_path = os.path.abspath('./caches/'+ hsh+'.jpg')
        if not os.path.exists(img_path):
            req = requests.get(BASEDOMAIN+url)
            with open(img_path, 'wb') as img_file:
                img_file.write(req.content)
            print('Cached '+hsh+'.jpg')
        return hsh+'.jpg'


def cached_json(BASEDOMAIN):
    time_now = time.strftime("%Y%m%d%H%M", time.localtime())
    if CACHEDJSON == {}:
        update_cache(BASEDOMAIN)
    elif int(CACHEDJSON['fullenddate']) <= int(time_now):
        update_cache(BASEDOMAIN)
    return CACHEDJSON


def update_cache(BASEDOMAIN):
    global CACHEDJSON
    req = requests.get(BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=-1&n=1')  # 默认第二天/今天
    CACHEDJSON = req.json()['images'][0]  # 改进写法，优化性能
    CACHEDJSON['fullenddate'] = CACHEDJSON['enddate'] + CACHEDJSON['fullstartdate'][-4:-1] # 取出具体时间（分钟），为最后 4 位
    print('Updated Cache!')


def cache_today():
    BASEDOMAIN = 'https://global.bing.com'
    req = requests.get(BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=-1&n=1')  # 默认第二天/今天
    pic_info = req.json()['images'][0]  # 改进写法，优化性能
    cache(pic_info, BASEDOMAIN)


def reload_cache():
    global CACHEDJSON
    CACHEDJSON = {}


if __name__ == '__main__':
    cache_today()