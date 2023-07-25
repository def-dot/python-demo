# 多进程要快于多线程?
import asyncio
import os
import threading
import time

import aiohttp
import requests
from concurrent.futures import ThreadPoolExecutor, wait, ProcessPoolExecutor, as_completed

from common import cost


def get_url(url):
    # raise Exception("error")
    res = requests.get(url)
    return url


class ThreadT:
    def thread_t(self):
        def func():
            print(1)

        t = threading.Thread(target=func)
        t.start()
        # for i in range(5):  # RuntimeError: threads can only be started once
        #     t.start()

    @cost
    def thread_pool_t(self, urls):
        t = ThreadPoolExecutor(max_workers=5)
        tasks = []
        for url in urls:
            tasks.append(t.submit(get_url, url))
        done, pending = wait(tasks)  # 等待所有任务完成
        print('done......')
        for i in done:
            # print(i.result())
            pass

    @cost
    def thread_as_completed_t(self, urls):
        t = ThreadPoolExecutor(max_workers=5)
        tasks = []
        for url in urls:
            tasks.append(t.submit(get_url, url))
        f = as_completed(tasks)  # as_completed返回生成器,生成器循环返回执行完的task
        print('done......')
        for i in f:
            print('111')
        print('over')



class ProcessT:
    @cost
    def process_t(self, urls):
        t = ProcessPoolExecutor()
        tasks = []
        for url in urls:
            tasks.append(t.submit(get_url, url))
        done, pending = wait(tasks)  # 等待所有任务完成
        for i in done:
            # print(i.result())
            pass


class BlockT:
    @cost
    def sync_t(self, urls):
        for url in urls:
            get_url(url)


class AsyncT:
    @cost
    def async_t(self, urls):
        async def get_url(client, url):
            async with client.get(url=url) as response:
                return await response.text()

        async def get_urls(urls):
            async with aiohttp.ClientSession() as client:
                tasks = [get_url(client, i) for i in urls]
                done, pending = await asyncio.wait(tasks)
                for i in done:
                    # print(i.result())
                    pass

        loop = asyncio.get_event_loop()
        loop.run_until_complete(get_urls(urls))
        # asyncio.run(get_urls(urls))


class ConcurrentFileT:
    def rw_file(self, input):
        print(f" {input} {os.getpid()}")
        with open('t.txt', 'a+') as f:
            for i in range(10):
                if input == '*' and i == 5:
                    time.sleep(1)
                f.write(input)
                time.sleep(0.1)
        return input

    def process_rw_file(self):
        # 多进程读写一个文件
        t = ProcessPoolExecutor()
        tasks = []
        tasks.append(t.submit(rw_file, "*"))
        # time.sleep(1)
        tasks.append(t.submit(rw_file, "#"))
        done, pending = wait(tasks)  # 等待所有任务完成
        print('over')
        for i in done:
            print("result " + i.result())
            pass


if __name__ == "__main__":
    urls = ["https://www.baidu.com"] * 10
    # ThreadT().thread_t()
    # ThreadT().thread_pool_t(urls)  # 2.22
    ThreadT().thread_as_completed_t(urls)
    # ProcessT().process_t(urls)  # 1.16
    # BlockT().sync_t(urls)  # 11.76
    # AsyncT().async_t(urls)  # (100 0.18)  (10000 3.85) (20000 8.08)
    # process_rw_file()
