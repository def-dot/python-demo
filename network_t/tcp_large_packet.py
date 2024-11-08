import socket
import struct

def send_large_tcp_packet(server_ip, server_port, data_size):
    # 创建一个 TCP 套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)

    try:
        # 构建一个大于 MTU 的字节数组
        large_data = b'A' * data_size

        # 发送数据
        client_socket.sendall(large_data)

    finally:
        # 关闭连接
        client_socket.close()

# 使用示例，模拟发送一个大于 MTU 的数据包（比如 2000 字节）
server_ip = '192.168.2.206'  # 服务器 IP 地址
server_port = 12345      # 服务器端口
data_size = 20000         # 模拟的数据包大小

send_large_tcp_packet(server_ip, server_port, data_size)
