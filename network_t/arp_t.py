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


if __name__ == '__main__':
    r = local_mac("192.168.2.42")
    print(f"local_mac {r}")

    r = remote_mac("152.32.190.242")  # arp作用于局域网，跨网络会一直等待
    print(f"remote_mac {r}")

