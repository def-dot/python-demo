import sys
import time


class SocketT:
    def client_t(self):
        import socket
        # 创建UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 服务器地址和端口
        server_address = ('45.156.109.47', 11111)

        # 发送数据到服务器
        message = 'stats'
        sock.sendto(message.encode(), server_address)

        # 接收服务器的响应
        data, address = sock.recvfrom(1024)  # 一次最多接收1024字节的数据
        print('接收到来自', address, '的响应:', data.decode())

        # 关闭socket连接
        sock.close()

    def server_t(self):
        import socket
        # 创建UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 绑定服务器地址和端口
        server_address = ('0.0.0.0', 12345)
        sock.bind(server_address)

        # 接收数据并发送响应
        while True:
            print('等待接收数据...')
            data, address = sock.recvfrom(1024)  # 一次最多接收1024字节的数据
            print('接收到来自', address, '的数据:', data.decode())

            # 发送响应数据
            response = 'Hello, client!'
            sock.sendto(response.encode(), address)


from scapy.all import *
class ScapyT:
    def client_t(self):
        # 创建UDP数据包
        packet = IP(dst='156.232.11.125') / UDP(dport=12345) / Raw(load='hello, server')

        # 发送数据包并接收响应
        response = sr1(packet, timeout=5)

        # 处理接收到的响应
        if response:
            print(response.summary())
        else:
            print("No response received.")

    def server_t(self):
        # 定义回调函数处理接收到的数据包
        def handle_packet(packet):
            if packet.haslayer(UDP):
                # 提取源IP地址、源端口号和数据
                src_ip = packet[IP].src
                src_port = packet[UDP].sport
                data = packet[Raw].load.decode('utf-8')

                # 打印接收到的数据包信息
                print(f"Received packet from {src_ip}:{src_port}")
                print(f"Data: {data}")

                # 构造响应数据包
                response = IP(dst=src_ip) / UDP(dport=src_port) / Raw(load="Response")

                # 发送响应数据包
                send(response)

        # 启动监听并捕获数据包
        sniff(filter="udp", prn=handle_packet)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "server":
        SocketT().server_t()
    else:
        SocketT().client_t()
