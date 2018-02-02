# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
requests.packages.urllib3.disable_warnings()

verifyheaders = {
    "Host": "wangpan007.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://wangpan007.com/share/kw%E6%9D%83%E5%8A%9B%E7%9A%84",
    "Accept-Encoding": "gzip, deflate, br",
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
url = "https://wangpan007.com/share/file/4842079"


def verifyt(url):
    r = requests.get(url, headers=verifyheaders, verify=False)
    r.encoding = "utf-8"
    text = r.text
    soup = bs(text, "html.parser")
    div = soup.find("div", class_="mt15")
    link = div.find_all("a", class_="btn btn_redirect")[0]['href']
    waiturl = "https://wangpan007.com" + link  # 获取真实的百度云链接
    # 对获取的百度云链接进行验证，判断内容是否失效
    s = requests.Session()
    newr = s.get(waiturl, verify=False,
                        headers=baiduheaders, allow_redirects=True)
    newr.encoding = "utf-8"  # 修改编码
    baidutext = newr.text
    print(baidutext)
    baidudsoup = bs(baidutext, 'html.parser')
    baidutitle = baidudsoup.find("div",id_="tip_msg")
    print(baidutitle)
    print(baidutitle.find_all("p")[1])


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

verifyt(url)
