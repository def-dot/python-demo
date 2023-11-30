from scapy.all import *


def local_mac(dst_ip):
    a = ARP()
    # a.show()
    src_mac = a[ARP].hwsrc
    # print(f"src mac {src_mac}")
    a.pdst = dst_ip
    recv = sr1(a)
    dst_mac = recv[ARP].hwsrc
    # print(f"dst mac {mac}")
    return dst_mac


def remote_mac(dst_ip):
    a = ARP()
    # a.show()
    src_mac = a[ARP].hwsrc
    # print(f"src mac {src_mac}")
    a.pdst = dst_ip
    recv = sr1(a)
    dst_mac = recv[ARP].hwsrc
    # print(f"dst mac {mac}")
    return dst_mac


def arp_request_t():
    """
    arp请求远程主机
    :return:
    """
    from scapy.all import Ether, ARP, srp

    # 构造 ARP 请求包
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst="192.168.2.200")

    # 发送 ARP 请求并接收响应
    result, unanswered = srp(packet, timeout=2, verbose=False)

    # 处理响应结果
    for sent, received in result:
        print(received.sprintf("MAC地址: %Ether.src%, IP地址: %ARP.psrc%"))


if __name__ == '__main__':
    # r = local_mac("192.168.2.42")
    # print(f"local_mac {r}")
    #
    # r = remote_mac("152.32.190.242")  # arp作用于局域网，跨网络会一直等待
    # print(f"remote_mac {r}")

    arp_request_t()