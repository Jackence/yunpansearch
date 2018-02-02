# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
import urllib.request
# from verify import verifyt
requests.packages.urllib3.disable_warnings()


headers = {
    "Host": "wangpan007.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://wangpan007.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}


def inputprocess(name):
    return urllib.request.quote(name)

linklist=[]
name="权力的游戏"
url = "https://wangpan007.com/share/kw"+inputprocess(name)
r = requests.get(url,headers=headers,verify=False)
text = r.text
soup = bs(text,"html.parser")
lists = soup.find("div",class_="list-wrap")
boxs = lists.find_all("div",class_="info-box")
for box in boxs:
    link = box.find("a")['href']
    newlink = "https://wangpan007.com"+link
    linklist.append(newlink)



