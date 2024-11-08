# """
# 测试主线程和子线程：主线程异常，存在子线程：子线程非守护线程(daemon=False，默认)时，主线程异常后，子线程仍然正常运行；子线程守护线程(daemon=True)时，主线程异常后，程序立即退出，子线程不再运行。
# 子线程异常不会影响主线程
# """
# import threading
# import time


# def test():
#     while True:
#         time.sleep(10)

# if __name__ == "__main__":
#     # thr = threading.Thread(target=test)
#     # thr.start()
#     print(1)
#     exit()
#     # raise Exception("no")


import threading
import time

def child_thread():
    for i in range(3):
        print("子线程正在运行")
        time.sleep(1)
    raise Exception("子线程发生异常")


thread = threading.Thread(target=child_thread)
# thread.daemon = True
thread.start()
while True:
    print("主线程正在运行")
    time.sleep(1)

