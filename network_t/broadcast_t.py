# """
# 广播测试
# """
# import socket
#
#
# def main():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#
#     message = "hello world"
#     try:
#         sent_bytes = sock.sendto(message.encode('utf-8'), ('172.16.255.255', 8888))
#         print(f"broadcast success {sent_bytes}")
#     except Exception as e:
#         print(f"broadcast error： {str(e)}")
#     finally:
#         sock.close()
#
#
def brocast_t():
    import socket
    # 创建一个UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定到广播地址和端口
    sock.bind(('0.0.0.0', 12345))

    # 设置套接字选项，允许发送广播包
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        # 接收广播包
        data, addr = sock.recvfrom(1024)

        # 打印接收到的广播包内容
        print("Received broadcast from {}: {}".format(addr, data.decode()))

        # 回复广播包
        reply = "This is a broadcast reply"
        sock.sendto(reply.encode(), addr)


if __name__ == '__main__':
    brocast_t()
