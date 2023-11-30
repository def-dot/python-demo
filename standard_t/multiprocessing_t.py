import multiprocessing
import threading


# queue = multiprocessing.Queue()


def worker(queue):
    print(f"worker {id(queue)}")
    data = queue.get()
    print(f'worker get {data}')


def multiprocessing_t():
    queue = multiprocessing.Queue()
    print(f"main {id(queue)}")
    queue.put("test")
    process = multiprocessing.Process(target=worker, args=(queue,))
    process.start()
    process.join()


def thread_t():
    queue = multiprocessing.Queue()
    print(f"main {id(queue)}")
    queue.put("test")
    thread = threading.Thread(target=worker, args=(queue,))
    thread.start()
    thread.join()


if __name__ == '__main__':
    multiprocessing_t()
    # thread_t()
    print('over')
