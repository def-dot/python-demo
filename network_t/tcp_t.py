from scapy.layers.inet import IP, TCP
from scapy.all import *


class TcpT:
    def syn(self):
        # TCP SYN包
        packet = IP(dst='192.168.13.236') / TCP(dport=3000, flags="S")
        response = sr1(packet, timeout=5)
        if response:
            print(response)
            if response.haslayer(TCP) and response.getlayer(TCP).flags == "SA":
                print('端口开放')
            else:
                print("端口关闭或过滤")
        else:
            print('无响应')

    def ack(self):
        # TCP ACK包
        packet = IP(dst='192.168.13.236') / TCP(dport=8000, flags="A")
        response = sr1(packet, timeout=10)
        if response:
            print(response)
            if response.haslayer(TCP):
                if response.getlayer(TCP).flags == 4:
                    print('端口关闭或过滤')
                elif response.getlayer(TCP).flags == 20:
                    print("端口开放")
            else:
                print("非TCP响应")
        else:
            print('无响应')

    def src(self):
        # 构建 TCP 包
        # ip = IP(src="192.168.2.240", dst="192.168.13.236")
        ip = IP(src="192.168.2.240", dst="156.232.11.125")
        tcp = TCP(sport=1234, dport=3000, flags="S", seq=1000)
        # 发送包
        packet = ip / tcp

        response = sr1(packet)
        # 打印返回的数据包信息
        if response:
            response.show()
        else:
            print("No response received.")


if __name__ == "__main__":
    TcpT().syn()
    # TcpT().src()
    # TcpT().ack()
