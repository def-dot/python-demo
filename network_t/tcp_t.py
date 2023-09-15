from scapy.layers.inet import IP, TCP
from scapy.all import *


class TcpT:
    def syn(self):
        # TCP SYN包
        packet = IP(dst='192.168.13.236') / TCP(dport=8000, flags="S")
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


if __name__ == "__main__":
    TcpT().syn()
    # TcpT().ack()
