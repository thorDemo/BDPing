# -*-coding=utf-8 -*-
from myLibs.BDPing import BDPing
from threadpool import ThreadPool, makeRequests
from random import sample


def start(url):
    BD = BDPing()
    if BD.ping('http://%s' % url):
        print('\033[36;1m提交成功 http://%s' % url)
    del BD


def get_char(num):
    chars = 'zyxwvutsrqponmlkjihgfedcba'
    result = ''.join(sample(chars, num))
    return result


def all_in():
    pool = ThreadPool(32)
    num = 100 * 10000
    BD = BDPing()
    urls = []
    arg = []
    temp = 1
    y = 0
    for x in range(0, num):
        url = 'http://b2c.958shop.com/cluni%s/%s.html' % (get_char(4), get_char(6))
        urls.append(url)
        if x % 50 == 0:
            arg.append(urls)
            if y == 32:
                requests = makeRequests(BD.ping_all_new, arg)
                [pool.putRequest(req) for req in requests]
                pool.wait()
                print('发送第 %s 个包 每个包： %s 总计： %s ' % (temp, 32, temp * 32))
                y = 0
                arg = []
            temp += 1
            y += 1
            urls = []


def only_one(x):
    pool = ThreadPool(32)
    urls = []
    file = open('domain.txt', 'r+')
    for line in file:
        urls.append('www.%s/' % line.strip('\n'))
        urls.append('www.%s/show/20180907%s.html' % (line.strip('\n'), get_char(5)))
    requests = makeRequests(start, urls)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    print('------------------------------********** 已经完成 %s 条 ***********------------------------------ ' % x * 1000)
    x += 1


if __name__ == '__main__':
    all_in()
