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
    def server_level_t(self):
        # 默认水平触发模式， epoll.poll(1) 可以重复读取事件（类似get），直到事件完成或事件状态改变
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

    def server_edge_t(self):
        # 边缘触发模式， epoll.poll(1) 事件只会读取一次（类似pop），所以在处理程序中，需要一次性处理完所有的数据
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", 9999))
        s.listen(1)
        s.setblocking(0)

        epoll = select.epoll()
        epoll.register(s.fileno(), select.EPOLLIN | select.EPOLLET)

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
                        try:
                            while True:  # 是否会阻塞进程？？？
                                sock, addr = s.accept()
                                sock.setblocking(0)
                                connections[sock.fileno()] = sock
                                epoll.register(sock.fileno(), select.EPOLLIN | select.EPOLLET)  # 立马可读？
                                requests[sock.fileno()] = request
                                responses[sock.fileno()] = response
                        except socket.error:
                            pass
                    elif event & select.EPOLLIN:
                        try:
                            while True:
                                requests[fileno] += connections[fileno].recv(1024)
                        except socket.error:
                            pass
                        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                            epoll.modify(fileno, select.EPOLLOUT | select.EPOLLET)
                            print(requests[fileno].decode('utf-8'))
                    elif event & select.EPOLLOUT:
                        try:
                            while responses[fileno] != '':
                                offset = connections[fileno].send(responses[fileno])  # send是从用户空间到内核缓冲区，还是从内核缓冲区到网卡
                                responses[fileno] = responses[fileno][offset:]
                        except socket.error:
                            pass
                        if responses[fileno] == '':
                            epoll.modify(fileno, select.EPOLLET)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                    elif event & select.EPOLLHUP:
                        epoll.unregister(fileno)
                        connections[fileno].close()
                        del connections[fileno]
        finally:
            epoll.unregister(s.fileno())
            epoll.close()
            s.close()

    def server_cork_t(self):
        # 默认水平触发模式， epoll.poll(1) 可以重复读取事件（类似get），直到事件完成或事件状态改变
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
                            connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)  # 开启TCP_CORK，send时报文大小达到MSS时，才发送
                            print(requests[fileno].decode('utf-8'))
                    elif event & select.EPOLLOUT:
                        offset = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][offset:]
                        if responses[fileno] == '':
                            connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 0)  # 关闭TCP_CORK
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

    def server_nodelay_t(self):
        # 默认水平触发模式， epoll.poll(1) 可以重复读取事件（类似get），直到事件完成或事件状态改变
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", 9999))
        s.listen(1)
        s.setblocking(0)
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

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
    BlockT().block_t()
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
    # EpoolT().server_level_t()
    # EpoolT().server_edge_t()
