import socket
from concurrent import futures
from common import cost


@cost
def block_t():
    def get_url_block():
        # 阻塞IO
        s = socket.socket()
        s.connect(("www.baidu.com", 80))
        req = "GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n"
        s.send(req.encode("utf-8"))
        res = b""
        chunk = s.recv(4096)
        while chunk:
            res += chunk
            chunk = s.recv(4096)
        # print(res.decode("utf-8"))
    for i in range(100):
        get_url_block()


@cost
def nonblock_t():
    def get_url_nonblock():
        # 非阻塞IO
        s = socket.socket()
        s.setblocking(False)
        try:
            s.connect(("www.baidu.com", 80))
        except BlockingIOError:
            pass
        req = "GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n"
        while True:
            try:
                s.send(req.encode("utf-8"))
                break
            except OSError as e:
                # print("send error.....")
                pass
        res = b""
        while True:
            try:
                chunk = s.recv(4096)
                while chunk:
                    res += chunk
                    chunk = s.recv(4096)
                break
            except OSError as e:
                # print("recv error.....")
                pass
        # print(res.decode("utf-8"))

    for i in range(100):
        get_url_nonblock()


@cost
def multi_block_t():
    def get_url_block():
        # 阻塞IO
        s = socket.socket()
        s.connect(("www.baidu.com", 80))
        req = "GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n"
        s.send(req.encode("utf-8"))
        res = b""
        chunk = s.recv(4096)
        while chunk:
            res += chunk
            chunk = s.recv(4096)
        # print(res.decode("utf-8"))
    p = futures.ProcessPoolExecutor()
    for i in range(100):
        p.submit(get_url_block)


if __name__ == "__main__":
    block_t()
    nonblock_t()
