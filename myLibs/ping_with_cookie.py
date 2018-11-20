# -*- coding=utf-8 -*-
import urllib3
from random import randint
from myTools.push_tools import PushTool
import requests
from threadpool import makeRequests, ThreadPool
import traceback

success_count = 0
failure_count = 0
cookie = PushTool.get_cookies()


class BDPing:

    @staticmethod
    def bd_ping_one(domain):
        global success_count
        global failure_count
        xml = """
            <?xml version="1.0"?>
            <methodCall>
            <methodName>weblogUpdates.ping</methodName>
            <params>
            <param>
            <value><string>%s</string></value>
            </param><param><value><string>%s</string></value>
            </param>
            </params>
            </methodCall>
            """
        while True:
            url = PushTool.get_url(domain)
            xml = xml.replace('%s', url)
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Content-Type': 'text/xml',
                'Connection': 'keep-alive',
                'User-Agent': PushTool.user_agent(),
                'Content-Length': str(len(xml)),
                'Host': 'ping.baidu.com',
                'Origin': 'http://ping.baidu.com',
                'Referer': 'http://ping.baidu.com/ping.html'
            }
            conn = requests.Session()
            conn.headers = headers
            # print(headers)
            # 将cookiesJar赋值给会话
            cookiesJar = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
            conn.cookies = cookiesJar
            code = 404
            try:
                res = conn.post('http://ping.baidu.com/ping/RPC2', headers=headers, json=xml, timeout=3.0)
                code = res.status_code
                if code == 200:
                    success_count += 1
                    if '<int>0</int>' in res.text:
                        print('成功 ping: %s status: %s' % (url, code))
                    else:
                        print('失败 ping: %s status: %s' % (url, code))
                else:
                    failure_count += 1
            except:
                failure_count += 1
            print('----------------------')
            print('success:%d  failure:%d' % (success_count, failure_count))

    @staticmethod
    def bd_ping_two(domain):
        global success_count
        global failure_count
        xml = """
            <?xml version="1.0"?>
            <methodCall>
            <methodName>weblogUpdates.ping</methodName>
            <params>
            <param>
            <value><string>%s</string></value>
            </param><param><value><string>%s</string></value>
            </param>
            </params>
            </methodCall>
            """
        while True:
            url = PushTool.rand_url(domain)
            xml = xml.replace('%s', url)
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Content-Type': 'text/xml',
                'Connection': 'keep-alive',
                'User-Agent': PushTool.user_agent(),
                'Content-Length': str(len(xml)),
                'Host': 'ping.baidu.com',
                'Origin': 'http://ping.baidu.com',
                'Referer': 'http://ping.baidu.com/ping.html'
            }
            conn = requests.Session()
            conn.headers = headers
            # print(headers)
            # 将cookiesJar赋值给会话
            cookiesJar = requests.utils.cookiejar_from_dict(cookie, cookiejar=None, overwrite=True)
            conn.cookies = cookiesJar
            code = 404
            try:
                res = conn.post('http://ping.baidu.com/ping/RPC2', headers=headers, json=xml, timeout=3.0)
                code = res.status_code
                if code == 200:
                    success_count += 1
                    if '<int>0</int>' in res.text:
                        print('成功 ping: %s status: %s' % (url, code))
                    else:
                        print('失败 ping: %s status: %s' % (url, code))
                else:
                    failure_count += 1
            except:
                failure_count += 1
            print('----------------------')
            print('success:%d  failure:%d' % (success_count, failure_count))

