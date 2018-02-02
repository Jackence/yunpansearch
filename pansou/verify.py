# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
import gevent
import gevent.monkey
gevent.monkey.patch_socket()

requests.packages.urllib3.disable_warnings()

baiduheaders = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}


def verifyt(waiturl):
    newr = requests.get(waiturl, verify=False, headers=baiduheaders)
    newr.encoding = "utf-8"  # 修改编码
    baidutext = newr.text
    baidudsoup = bs(baidutext, 'html.parser')
    baidutitle = baidudsoup.find("title")
    if (baidutitle.text == "百度网盘-链接不存在"):
        print(baidutitle)
        status = "no"
        return 0
    elif(baidutitle.text == "页面不存在"):
        print(baidutitle)
        status = "no"
        return 0
    elif(baidutitle.text == "百度网盘 个人专辑 - 百度网盘，让美好永远陪伴"):
        print(baidutitle)
        status = "no"
        return 0
    else:
        print(baidutitle)
        status = "yes"
        return waiturl

