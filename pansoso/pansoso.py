# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
import urllib.request
requests.packages.urllib3.disable_warnings()

headers = {
    "Host": "www.pansoso.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",

}


def inputprocess(name):
    return urllib.request.quote(name)


def process(proname, pageno, linklistpansoso):
    url = "http://www.pansoso.com/zh/" + proname + "_" + str(pageno)
    r = requests.get(url, verify=False, headers=headers)
    soup = bs(r.text, "html.parser")
    divs = soup.find_all("div", class_="pss")
    for div in divs:
        if(div):
            link = div.find("a")['href']
            url = "http://www.pansoso.com" + link
            linklistpansoso.append(url)
    pageno += 1
    if(pageno >= 9):
        return linklistpansoso
    else:
        try:
            process(proname, pageno, linklistpansoso)
        except:
            return linklistpansoso
