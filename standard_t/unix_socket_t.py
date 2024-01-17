# 域套接字
import socket
import os
import sys

# 定义UNIX域套接字路径
socket_path = "/tmp/my_unix_socket"


def server_t():
    # 如果套接字文件存在，删除它
    if os.path.exists(socket_path):
        os.remove(socket_path)

    # 创建UNIX域套接字
    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(socket_path)
    server_socket.listen(1)

    print(f"Server listening on {socket_path}")

    # 等待客户端连接
    client_socket, client_address = server_socket.accept()
    print(f"Connected by: {client_address}")

    # 接收消息并回复
    data = client_socket.recv(1024)
    print(f"Received message: {data.decode()}")

    response = "Hello, client! This is the server."
    client_socket.send(response.encode())

    # 关闭套接字
    client_socket.close()
    server_socket.close()


def client_t():
    # 创建UNIX域套接字
    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # 连接到服务端
    client_socket.connect(socket_path)

    # 发送消息
    message = "Hello, server! This is the client."
    client_socket.send(message.encode())

    # 接收回复消息
    response = client_socket.recv(1024)
    print(f"Received response: {response.decode()}")

    # 关闭套接字
    client_socket.close()


if __name__ == "__main__":
    if sys.argv[1] == "client":
        client_t()
    else:
        server_t()
