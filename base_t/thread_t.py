import time

import requests
from concurrent.futures import ThreadPoolExecutor, wait, ProcessPoolExecutor, as_completed


def get_url(url):
    res = requests.get(url)
    time.sleep(1)
    print("completed")
    return res


def thread_test(urls):
    time1 = time.time()
    t = ThreadPoolExecutor(max_workers=2)
    # with ThreadPoolExecutor(max_workers=2) as t:
    tasks = []
    for url in urls:
        tasks.append(t.submit(get_url, url))
    # wait(tasks)  # 等待所有任务完成
    # as_completed 只要有任务完成就输出
    # for future in as_completed(tasks):
    #     data = future.result()
    #     print("result %s" % data)
    # for future in tasks:
    #     print(future.done())

    time2 = time.time()
    print("thread pool cost %s" % (time2-time1))


def process_test(urls):
    time1 = time.time()
    with ProcessPoolExecutor() as t:
        tasks = []
        for url in urls:
            tasks.append(t.submit(get_url, url))
        wait(tasks)
    time2 = time.time()
    print("thread pool cost %s" % (time2-time1))


def sync_test(urls):
    time1 = time.time()
    for url in urls:
        get_url(url)
    time2 = time.time()
    print("sync cost %s" % (time2 - time1))


if __name__ == "__main__":
    urls = ["https://www.baidu.com"] * 10
    thread_test(urls)  # 0.35
    # sync_test(urls)  # 11.54
    print("over")
