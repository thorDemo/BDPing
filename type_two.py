from myLibs.ping_with_cookie import BDPing
from threadpool import ThreadPool, makeRequests

if __name__ == '__main__':
    pool = ThreadPool(32)
    arg = []
    for x in range(0, 32):
        arg.append('http://d.958shop.com/bbkni')
    request = makeRequests(BDPing.bd_ping_two, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()