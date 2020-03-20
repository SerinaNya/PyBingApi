import os
import requests
AUTOCACHE = True


def cache(json_info, BASEDOMAIN):
    if AUTOCACHE:
        url = json_info['url']
        hsh = json_info['hsh']
        img_path = os.path.abspath('./caches/' + hsh + '.jpg')
        if not os.path.exists(img_path):
            req = requests.get(BASEDOMAIN+url)
            with open(img_path, 'wb') as img_file:
                img_file.write(req.content)
            print('Cached '+hsh+'.jpg')


def cache_today():
    BASEDOMAIN = 'https://global.bing.com'
    req = requests.get(BASEDOMAIN+'/HPImageArchive.aspx?format=js&idx=-1&n=1')  # 默认第二天/今天
    pic_info = req.json()['images'][0]  # 改进写法，优化性能
    cache(pic_info, BASEDOMAIN)


if __name__ == '__main__':
    cache_today()