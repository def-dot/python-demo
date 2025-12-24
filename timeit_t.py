"""
测量代码执行时间
"""
import time
from timeit import default_timer


if __name__ == "__main__":
    t_start = default_timer()
    time.sleep(1)
    t_end = default_timer()
    print(t_end - t_start)
