# coding:utf-8
from pansoso.pansoso import process
from pansou.pansou import inputprocess, processdata
from sopanpan.sopanpan import urlprocess
import requests
import re
from bs4 import BeautifulSoup as bs
import gevent
import gevent.monkey
gevent.monkey.patch_socket()
requests.packages.urllib3.disable_warnings()
from verify import directpansoso, directsopanpan, verifyt


name = input("input search name:")
pageno = 1

# pansou站点处理
linklistpansou = []
processdata(name, pageno, linklistpansou)  # 不需要跳转的

# pansoso站点处理
linklistpansoso = []
process(inputprocess(
    name), pageno, linklistpansoso)  # 需要跳转的


# sopanpan站点处理
linklistsopanpan = []
linklist2 = urlprocess(inputprocess(name), linklistsopanpan)  # 需要跳转的


linklist0 = []
# 将跳转换成真正的百度云链接
task0 = [gevent.spawn(directpansoso, link1, linklist0)
         for link1 in linklistpansoso]
gevent.joinall(task0)

linklist1 = []
task1 = [gevent.spawn(directsopanpan, link2, linklist1)
         for link2 in linklistsopanpan]
gevent.joinall(task1)


# 对未失效的链接进行去重 linklist0,linklist1和linklistpansou


linkall = linklist0 + linklist1 + linklistpansou

# print(linkall)
formatlist = list(set(linkall))
formatlist.sort(key=linkall.index)
# print(formatlist)
# 处理所有的链接，判断有用的链接，收录起来
linkused = []
tasks = [gevent.spawn(verifyt, linkn, linkused) for linkn in formatlist]
gevent.joinall(tasks)
print(linkused)
