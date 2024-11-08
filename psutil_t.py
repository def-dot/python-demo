# 获取系统资源（CPU、内存、硬盘、网络）信息，进程信息。

import psutil
import time

if __name__ == "__main__":
    print(psutil.cpu_count())  # CPU核心数（指的是逻辑线程数，超线程技术下，一个物理核心可以有两个逻辑线程）
    print(psutil.cpu_percent())  
    r = psutil.process_iter()
    x = []
    for i in r:
        x.append(i)
    print(len(x))
    old_info = psutil.net_io_counters(pernic=True)
    print(old_info)
    time.sleep(1)
    new_info = psutil.net_io_counters(pernic=True)
    print(new_info)

