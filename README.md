# PyBingApi

![Python3](https://img.shields.io/badge/Python-3-blue?color=3776AB&&logo=python) ![GPLv3](https://img.shields.io/github/license/jinzhijie/PyBingApi) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/jinzhijie/PyBingApi/master)

获取必应今日美图：Bing-API 的 Python3 实现，基于 Flask

## 我要怎么部署和使用这个 API？

PyBingAPI 对配置的要求非常低，只要有Python就能跑。

### 环境要求

- 一台主机
- Python 3
- **一个在线率 60% 以上的脑子**

### 部署教程

1. 检查你的主机是否符合运行 PyBingAPI 的环境要求
2. 把这个仓库克隆或下载
3. 执行 `pip3 install Flask`
4. 执行 `python3 app.py` 以启动

### 如何使用？

你可以在任何可以使用 URL 添加图片的地方引用 ``https://your-domain.com/bing``，会直接显示当天的Bing 今日美图。

``https://your-domain.com/bing/1-7``以获取历史一周内的 Bing 美图

``https://your-domain.com/bing/cache``以本地缓存的 Bing 美图(仅限当天缓存)



## **版权**

辣鸡 Bing 今日美图 API 是基于 GNU General Public License v3.0 开放源代码的自由软件，你可以遵照 GPLv3 协议来二次开发并发布这一程序。

而 Bing 今日美图为微软公司的产品，使用时请遵守相关规定及法律。**虽然获取到的图片上没有水印，但是我仍然建议你在醒目的地方加上一句“图片来自 Bing 今日美图”**。 

程序原作者为[@Xiao_Jin](https://xiao-jin.xyz/)，转载请注明。

感谢 [@MintTang](https://github.com/MintTang) 为我们提供 DEMO 托管！[点击查看 DEMO](https://api.kagurazakaeri.com/)
> 此为官方 DEMO
