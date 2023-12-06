"""
阻塞IO
"""

import datetime
import socket
import sys
import threading
import time


def handle_connection(client_socket):
    request = client_socket.recv(1024)
    time.sleep(5)
    # 处理请求并生成响应
    response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 13\r\n\r\nHello, World!"
    client_socket.sendall(response)
    client_socket.close()


def run_server():
    host = 'localhost'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    print(f"Serving on {host}:{port}...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]} {datetime.datetime.now()}")
        handle_connection(client_socket)


def run_client():
    host = 'localhost'
    port = 8888

    request = b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(request)

    response = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    client_socket.close()

    print(response.decode())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(5):
            t = threading.Thread(target=run_client)
            t.start()
    else:
        run_server()
