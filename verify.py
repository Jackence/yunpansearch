#coding:utf-8
import pansoso
import pansou
import sopanpan
import requests
import re
from bs4 import BeautifulSoup as bs
import gevent
import gevent.monkey
gevent.monkey.patch_socket()
requests.packages.urllib3.disable_warnings()


sopanpandirheaders = {#sopanpan 站点headers
    "Host": "www.sopanpan.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.sopanpan.com/search/%E6%9D%83%E5%8A%9B%E7%9A%84%E6%B8%B8%E6%88%8F-0-0.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "sopanpanwx=1; Hm_lvt_413b8e292048b1753606d3b7576446f3=1516524882,1516604831,1517397120,1517453196; UM_distinctid=1614f423d7a5a-0ccf90e409e982-4323461-1fa400-1614f423d7b1c1; Hm_lvt_66be306d99cad41c78b42980eb034651=1517453202; Hm_lpvt_66be306d99cad41c78b42980eb034651=1517453202; Hm_lpvt_413b8e292048b1753606d3b7576446f3=1517453238; CNZZDATA1261677980=799337431-1517453195-%7C1517453237; Hm_lvt_cb48bb397e3ec124a1cf1cee84008840=1516524899,1516604844,1517397158,1517453239; Hm_lpvt_cb48bb397e3ec124a1cf1cee84008840=1517453239"
}

dirheaderspansoso = {#pansoso 站点headers
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


baiduheaders = { #百度网盘headers
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

def directsopanpan(url,lists):#处理重定向--sopanpan 站点
    r = requests.get(url, verify=False, dirheaders=headers)
    text = r.text
    soup = bs(text, "html.parser")
    d = soup.find("div", class_="bcw radius_b dfinfo")
    waiturl = d.find("a", rel="noreferrer")['href']  # 获取真实的百度云链接
    lists.append(waiturl)
    return lists
    
def directpansoso(url,lists):#处理重定向--pansoso 站点
    r = requests.get(url, headers=dirheaderspansoso, verify=False)
    r.encoding = "utf-8"
    text = r.text
    soup = bs(text, "html.parser")
    div = soup.find("div", class_="down")
    link = div.find_all("a")[1]['href']
    waiturl = link.replace("www.pansoso.com/?a=go", "url.pansoso.com/?a=to")
    # 获取真实的百度云链接
    # print(waiturl)
    lists.append(waiturl)
    # print (lists)
    return lists


def verifyt(waiturl,linkn):
    # 对获取的百度云链接进行验证，判断内容是否失效
    newr = requests.get(waiturl, verify=False, headers=baiduheaders)
    newr.encoding = "utf-8"  # 修改编码
    baidutext = newr.text
    baidudsoup = bs(baidutext, 'html.parser')
    baidutitle = baidudsoup.find("title")
    if (baidutitle.text == "百度网盘-链接不存在"):
        # print(baidutitle)
        status = "no"
        return 0
    elif(baidutitle.text == "页面不存在"):
        # print(baidutitle)
        status = "no"
        return 0
    elif(baidutitle.text == "百度网盘 个人专辑 - 百度网盘，让美好永远陪伴"):
        # print(baidutitle)
        status = "no"
        return 0
    else:
        # print(baidutitle)
        status = "yes"
        linkn.append(waiturl)
        return linkn
