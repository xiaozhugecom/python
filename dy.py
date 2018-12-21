# 爬虫使用cookie
import json
from urllib import request
import urllib3
from http import cookiejar
import datetime
import time


if __name__ == '__main__':
    cookie = cookiejar.CookieJar()
    handler=request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('https://s.ruiyinxin.com/agent/ims/merch/list.do')
    url = "https://s.ruiyinxin.com/agent/ims/merch/list.do"
    headers = {
        # Cookie值从登录后的浏览器，拷贝，方法文章上面有介绍
        "Cookie": "JSESSIONID=EC587D8AAEED5AA79BDA77090045CC8D;SESSION=7341730e-656f-4adf-b254-7c44a7a02aa7"
    }
    req = request.Request(url=url,headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)
    jsons = json.loads(html)
    row = jsons["rows"]
    print(row)


# def doSth():
#     # 把爬虫程序放在这个类里
#
#     print(u'这个程序要开始疯狂的运转啦')
#
#
# # 一般网站都是1:00点更新数据，所以每天凌晨一点启动
# def main(h=13, m=11):
#     while True:
#         now = datetime.datetime.now()
#         # print(now.hour, now.minute)
#         if now.hour == h and now.minute == m:
#             doSth()
#         # 每隔60秒检测一次
#         time.sleep(60)
#         print(time.sleep(5*60*1000))
#
# main()

