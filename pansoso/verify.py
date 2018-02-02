# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
requests.packages.urllib3.disable_warnings()

verifyheaders = {
    "Host": "www.pansoso.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "http://www.pansoso.com/zh/%E6%9D%83%E5%8A%9B%E7%9A%84%E6%B8%B8%E6%88%8F",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

baiduheaders = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}


def verifyt(url):
    r = requests.get(url, headers=verifyheaders, verify=False)
    r.encoding = "utf-8"
    text = r.text
    soup = bs(text, "html.parser")
    div = soup.find("div", class_="down")
    link = div.find_all("a")[1]['href']
    waiturl = link.replace("www.pansoso.com/?a=go", "url.pansoso.com/?a=to")
# 获取真实的百度云链接
    # 对获取的百度云链接进行验证，判断内容是否失效
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
        return url
