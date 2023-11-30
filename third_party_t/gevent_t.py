import datetime
import time

import requests
import gevent


def fetch_t(url):
    requests.get(url)
    print(f'{datetime.datetime.now()}')


if __name__ == '__main__':
    t1 = time.time()
    urls = ['https://www.example.com'] * 100
    tasks = [gevent.spawn(fetch_t, url) for url in urls]
    gevent.joinall(tasks)
    print(f'cost {time.time() - t1}')
