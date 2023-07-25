import socket, select
import time
from concurrent import futures


class BlockT:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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


class TcpT:
    def recv_socket(self, sock, addr):
        print(f"accept new connection from {addr}")
        while True:
            data = sock.recv(1024)
            time.sleep(10)
            if not data:
                break
            print(data.decode('utf-8'))
        sock.close()
        print("over!")

    def server_t(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 9999))
        s.listen(2)  # backlog同时处理的请求数，超过数量的连接请求直接ConnectionRefusedError
        while True:
            sock, addr = s.accept()
            self.recv_socket(sock, addr)
            # t = threading.Thread(target=self.recv_socket, args=(sock, addr))
            # t.start()

    def client_t(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 9999))
        s.send(msg.encode('utf-8'))
        s.close()


class HttpT:
    def server_t(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", 9999))
        s.listen(1)


        EOL1 = b'\n\n'
        EOL2 = b'\n\r\n'
        response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
        response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
        response += b'Hello, world!'

        try:
            while True:
                sock, addr = s.accept()
                request = b''
                while EOL1 not in request and EOL2 not in request:
                    request += sock.recv(1024)
                print(request.decode('utf-8'))
                print("sending!!!")
                sock.send(response)
                sock.close()
                print("over!")
        finally:
            s.close()


class EpoolT:
    def server_t(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", 9999))
        s.listen(1)
        s.setblocking(0)

        epoll = select.epoll()
        epoll.register(s.fileno(), select.EPOLLIN)

        connections = {}
        requests = {}
        responses = {}

        EOL1 = b'\n\n'
        EOL2 = b'\n\r\n'
        request = b''
        response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
        response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
        response += b'Hello, world!'

        try:
            while True:
                events = epoll.poll(1)
                for fileno, event in events:
                    if fileno == s.fileno():
                        sock, addr = s.accept()
                        connections[sock.fileno()] = sock
                        epoll.register(sock.fileno(), select.EPOLLIN)  # 立马可读？
                        requests[sock.fileno()] = request
                        responses[sock.fileno()] = response
                    elif event & select.EPOLLIN:
                        requests[fileno] += connections[fileno].recv(1024)
                        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                            epoll.modify(fileno, select.EPOLLOUT)
                            print(requests[fileno].decode('utf-8'))
                    elif event & select.EPOLLOUT:
                        offset = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][offset:]
                        if responses[fileno] == '':
                            epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                    elif event & select.EPOLLHUP:
                        epoll.unregister(fileno)
                        connections[fileno].close()
                        del connections[fileno]
        finally:
            epoll.unregister(s.fileno())
            epoll.close()
            s.close()


if __name__ == "__main__":
    # BlockT().block_t()
    # BlockT().nonblock_t()
    # if sys.argv[1] == 'server':
    #     TcpT().server_t()
    # else:
    #     TcpT().client_t('zhangsan')
    #     TcpT().client_t('lisi')
    #     TcpT().client_t('wangwu')
    #     TcpT().client_t('maliu')
    #     TcpT().client_t('wuqi')
    #     TcpT().client_t('enba')
    #     TcpT().client_t('nijiu')
    # HttpT().server_t()
    EpoolT().server_t()
