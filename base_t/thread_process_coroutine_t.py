# 多进程要快于多线程?
import asyncio
import aiohttp
import requests
from concurrent.futures import ThreadPoolExecutor, wait, ProcessPoolExecutor, as_completed

from common import cost


def get_url(url):
    res = requests.get(url)
    return url


@cost
def thread_t(urls):
    t = ThreadPoolExecutor(max_workers=5)
    tasks = []
    for url in urls:
        tasks.append(t.submit(get_url, url))
    done, pending = wait(tasks)  # 等待所有任务完成
    for i in done:
        # print(i.result())
        pass


@cost
def thread_as_completed_t(urls):
    t = ThreadPoolExecutor(max_workers=5)
    tasks = []
    for url in urls:
        tasks.append(t.submit(get_url, url))
    f = as_completed(tasks)  # as_completed返回生成器,生成器循环返回执行完的task
    for i in f:
        # print(i.result())
        pass


@cost
def process_t(urls):
    t = ProcessPoolExecutor()
    tasks = []
    for url in urls:
        tasks.append(t.submit(get_url, url))
    done, pending = wait(tasks)  # 等待所有任务完成
    for i in done:
        # print(i.result())
        pass


@cost
def sync_t(urls):
    for url in urls:
        get_url(url)


@cost
def async_t(urls):
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


if __name__ == "__main__":
    urls = ["https://www.baidu.com"] * 20000
    # thread_t(urls)  # 2.22
    # thread_as_completed_t(urls)
    # process_t(urls)  # 1.16
    # sync_t(urls)  # 11.76
    async_t(urls)  # (100 0.18)  (10000 3.85) (20000 8.08)
