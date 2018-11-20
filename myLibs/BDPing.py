# -*- coding=utf-8 -*-
import urllib3
from random import randint


class BDPing:
    def __init__(self):
        self.http = urllib3.PoolManager(timeout=3.0)

    def get_proxy(self):
        return self.http.request('GET', 'http://127.0.0.1:5010/get/').data

    def delete_proxy(self, proxy):
        self.http.request('GET', "http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

    def ping(self, url):
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
        xml = (xml % (url, url))
        headers = {
            'Content-Type': 'text/xml',
            'User-Agent': 'request',
            'Content-Length': str(len(xml))
        }
        proxy = '\033[31;1m未获取到代理 IP !'
        try:
            proxy = 'http://%s' % str(self.get_proxy(), encoding='utf-8').strip('')
        except:
            print('\033[31;1m本地链接超时 重试！！！！！！')
            self.ping(url)
        print('\033[32;1m获取IP %s ' % proxy)
        while True:
            try:
                proxy_http = urllib3.ProxyManager(proxy)
                html = proxy_http.request('POST', 'http://ping.baidu.com/ping/RPC2',
                                          headers=headers, body=xml, timeout=3.0)
                # 使用代理访问
                if '<int>0</int>' in html.data.decode():
                    return True
            except Exception as e:
                print('\033[31;1m失败重试 ping %s' % url)
                self.ping(url)
                return False

    def ping_all(self, urls):

        agent = BDPing.user_agent()
        try:
            proxy = 'http://%s' % str(self.get_proxy(), encoding='utf-8').strip('')
            proxy_http = urllib3.ProxyManager(proxy)
        except:
            print('\033[31;1m本地链接超时 退出')
            return
        for url in urls:
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
            xml = (xml % (url, url))
            headers = {
                'Content-Type': 'text/xml',
                'User-Agent': agent,
                'Content-Length': str(len(xml)),
                'Host': 'ping.baidu.com',
                'Origin': 'http://ping.baidu.com',
            }
            try:
                html = proxy_http.request('POST', 'http://ping.baidu.com/ping/RPC2',
                                      headers=headers, body=xml, timeout=3.0)
                # 使用代理访问
                status = html.status
                if '<int>0</int>' in html.data.decode():
                    print('\033[32;1m成功 ping: %s status: %s ip: %s Agent: %s' % (url, status, proxy, agent))
                else:
                    print(html.data.decode())
                    print('\033[31;1m失败 ping: %s status: %s ip: %s Agent: %s' % (url, status, proxy, agent))

            except Exception as e:
                print('\033[31;1m失败 ping: %s status: %s ip: %s Agent: %s' % (url, 0, proxy, agent))
                return

    def ping_all_new(self, urls):
        agent = BDPing.user_agent()
        try:
            # proxy = 'http://%s' % str(self.get_proxy(), encoding='utf-8').strip('')
            # proxy_http = urllib3.ProxyManager(proxy)
            pass
        except:
            print('\033[31;1m本地链接超时 退出')
            return
        for url in urls:
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
            xml = (xml % (url, url))
            headers = {
                'Content-Type': 'text/xml',
                'User-Agent': agent,
                'Content-Length': str(len(xml)),
                'Host': 'ping.baidu.com',
                'Origin': 'http://ping.baidu.com',
                'Referer': 'http://ping.baidu.com/ping.html'
            }
            try:
                html = self.http.request('POST', 'http://ping.baidu.com/ping/RPC2',
                                          headers=headers, body=xml, timeout=3.0)
                # 使用代理访问
                status = html.status
                if '<int>0</int>' in html.data.decode():
                    print('\033[32;1m成功 ping: %s status: %s  Agent: %s' % (url, status, agent))
                    # print('\033[32;1m成功 ping: %s status: %s ip: %s Agent: %s' % (url, status, proxy, agent))
                else:
                    print('\033[31;1m失败 ping: %s status: %s  Agent: %s' % (url, status, agent))
                    # print('\033[31;1m失败 ping: %s status: %s ip: %s Agent: %s' % (url, status, proxy, agent))

            except Exception as e:
                print('\033[31;1m失败 ping: %s status: %s  Agent: %s' % (url, 0, agent))
                # print('\033[31;1m失败 ping: %s status: %s ip: %s Agent: %s' % (url, 0, proxy, agent))
                return

    @staticmethod
    def user_agent():
        all_agent = [
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                    'User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
                    'Opera/8.0 (Windows NT 5.1; U; en)'
                    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
                    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
                    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
                    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
                    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
                    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
                    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
                    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
                    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)',
                    ]

        return all_agent[randint(0,31)]