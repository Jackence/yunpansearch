# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
import urllib.request
requests.packages.urllib3.disable_warnings()
import json
headers = {
    "Host": "106.15.195.249:8011",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
}


def inputprocess(name):
    return urllib.request.quote(name)

# 获取链接
def processdata(name,pageno,linklist):
    url = "http://106.15.195.249:8011/search_new?callback=jQuery17208926134531683858_1517478952695&q=" + \
        inputprocess(name) + "&p="+str(pageno)+"&_=1517478953488"
    r = requests.get(url, headers=headers, verify=False)
    r.encoding="utf-8"
    text = (r.text)
    data = text.replace("jQuery17208926134531683858_1517478952695(","")
    d = data.replace("})","}")
    dals = json.loads(d)
    datas = dals['list']['data']
    for data in datas:
        urllink = data['link']
        linklist.append(urllink)

    if(pageno<=9):
        pageno+=1
        processdata(name,pageno,linklist) 
    else:
        return linklist



