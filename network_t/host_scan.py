import ipaddress


def arp_request_t():
    """
    arp广播请求
    pdst为ip或网段
    :return:
MAC地址: ec:da:59:53:bc:6b, IP地址: 192.168.2.1
MAC地址: 00:0c:29:9a:97:5e, IP地址: 192.168.2.2
MAC地址: 6c:92:bf:9b:dc:bf, IP地址: 192.168.2.3
MAC地址: 6c:92:bf:6b:d5:32, IP地址: 192.168.2.5
MAC地址: 00:50:56:9e:a7:84, IP地址: 192.168.2.7
MAC地址: 00:50:56:9e:ae:63, IP地址: 192.168.2.10
MAC地址: 00:0c:29:f2:12:11, IP地址: 192.168.2.12
MAC地址: 00:0c:29:94:42:eb, IP地址: 192.168.2.13
MAC地址: 00:50:56:9e:de:10, IP地址: 192.168.2.15
MAC地址: 00:0c:29:f2:cb:b6, IP地址: 192.168.2.11
MAC地址: 00:22:46:4e:ba:ab, IP地址: 192.168.2.26
MAC地址: 00:22:46:4e:ba:99, IP地址: 192.168.2.27
MAC地址: 00:0c:29:f4:15:21, IP地址: 192.168.2.31
MAC地址: 00:0c:29:46:4f:db, IP地址: 192.168.2.32
MAC地址: 00:0c:29:f1:22:31, IP地址: 192.168.2.33
MAC地址: d8:5e:d3:5a:2c:2b, IP地址: 192.168.2.41
MAC地址: 00:0c:29:ec:2b:68, IP地址: 192.168.2.45
MAC地址: b4:2e:99:86:41:a4, IP地址: 192.168.2.46
MAC地址: e8:9c:25:42:c2:75, IP地址: 192.168.2.52
MAC地址: 18:31:bf:0b:5b:2b, IP地址: 192.168.2.51
MAC地址: d8:5e:d3:5a:2c:6b, IP地址: 192.168.2.55
MAC地址: 18:c0:4d:2e:fb:d5, IP地址: 192.168.2.60
MAC地址: 48:ea:63:ec:81:03, IP地址: 192.168.2.63
MAC地址: 18:c0:4d:2e:f8:bc, IP地址: 192.168.2.76
MAC地址: 0c:9d:92:63:7c:ca, IP地址: 192.168.2.94
MAC地址: 40:6c:8f:2f:8f:45, IP地址: 192.168.2.96
MAC地址: 00:0c:29:f2:cb:b6, IP地址: 192.168.2.95
MAC地址: 6c:92:bf:9b:df:a7, IP地址: 192.168.2.4
MAC地址: 18:c0:4d:2e:f9:67, IP地址: 192.168.2.113
MAC地址: 0c:9d:92:63:74:69, IP地址: 192.168.2.117
MAC地址: 00:0c:29:e3:a6:bd, IP地址: 192.168.2.122
MAC地址: 00:0e:c6:c4:d9:98, IP地址: 192.168.2.124
MAC地址: 00:0c:29:9c:6a:aa, IP地址: 192.168.2.126
MAC地址: 0c:9d:92:63:74:68, IP地址: 192.168.2.128
MAC地址: d8:5e:d3:5b:cb:45, IP地址: 192.168.2.140
MAC地址: e0:d5:5e:f8:8e:a1, IP地址: 192.168.2.144
MAC地址: 00:0c:29:73:8a:b4, IP地址: 192.168.2.154
MAC地址: 00:0c:29:87:f7:86, IP地址: 192.168.2.157
MAC地址: 18:c0:4d:67:00:10, IP地址: 192.168.2.160
MAC地址: 48:57:02:65:64:60, IP地址: 192.168.2.6
MAC地址: 00:0c:29:9e:74:e6, IP地址: 192.168.2.177
MAC地址: b4:2e:99:e9:57:ec, IP地址: 192.168.2.179
MAC地址: 18:c0:4d:36:a4:1d, IP地址: 192.168.2.180
MAC地址: 08:00:27:eb:c4:3e, IP地址: 192.168.2.191
MAC地址: 00:0c:29:97:1f:59, IP地址: 192.168.2.198
MAC地址: 00:0c:29:de:59:6a, IP地址: 192.168.2.200
MAC地址: d8:5e:d3:5a:2c:1b, IP地址: 192.168.2.201
MAC地址: 00:0c:29:77:37:70, IP地址: 192.168.2.197
MAC地址: 00:0c:29:73:1f:2b, IP地址: 192.168.2.202
MAC地址: 0c:9d:92:63:7c:71, IP地址: 192.168.2.199
MAC地址: e8:61:1a:03:b3:f5, IP地址: 192.168.2.234
MAC地址: 6c:92:bf:9b:dc:bc, IP地址: 192.168.2.236
MAC地址: e8:61:1f:43:5c:cc, IP地址: 192.168.2.235
MAC地址: 6c:92:bf:9b:df:a4, IP地址: 192.168.2.237
MAC地址: 6c:92:bf:9b:df:a6, IP地址: 192.168.2.238
MAC地址: 6c:92:bf:9b:dc:be, IP地址: 192.168.2.239
MAC地址: 00:22:46:33:db:be, IP地址: 192.168.2.250
MAC地址: 18:c0:4d:3e:0d:df, IP地址: 192.168.2.251
    """
    from scapy.all import Ether, ARP, srp

    # 构造 ARP 请求包
    target_ip = "目标网络段的广播地址"
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst='192.168.2.200')

    # 发送 ARP 请求并接收响应
    result, unanswered = srp(packet, timeout=2, verbose=False)

    # 处理响应结果
    for sent, received in result:
        print(received.sprintf("MAC地址: %Ether.src%, IP地址: %ARP.psrc%"))


def ping_request_t():
    """
    ping请求
    pdst为ip或网段
    :return:
WARNING: Mac address to reach destination not found. Using broadcast.
WARNING: more Mac address to reach destination not found. Using broadcast.
WARNING: Mac address to reach destination not found. Using broadcast.
WARNING: Mac address to reach destination not found. Using broadcast.
存活主机: 192.168.2.1
存活主机: 192.168.2.2
存活主机: 192.168.2.3
存活主机: 192.168.2.4
存活主机: 192.168.2.5
存活主机: 192.168.2.6
存活主机: 192.168.2.7
存活主机: 192.168.2.10
存活主机: 192.168.2.11
存活主机: 192.168.2.13
存活主机: 192.168.2.15
    """
    from scapy.all import IP, ICMP, sr

    # 定义目标IP地址范围（使用CIDR表示法）
    target_ip_range = "192.168.2.0/28"

    # 构造ICMP Echo请求包
    packet = IP(dst=target_ip_range) / ICMP()

    # 发送ICMP Echo请求包并接收响应
    response, _ = sr(packet, timeout=2, verbose=False)

    # 处理响应结果
    for sent_packet, received_packet in response:
        if received_packet.haslayer(ICMP) and received_packet.getlayer(ICMP).type == 0:
            ip_address = received_packet.getlayer(IP).src
            print(f"存活主机: {ip_address}")


def tcp_syn_request_t():
    """
发送tcp syn包，收到syn-ack表明端口存活
存活主机 192.168.2.1:443
存活主机 192.168.2.3:443
存活主机 192.168.2.4:443
存活主机 192.168.2.5:443
存活主机 192.168.2.6:443
WARNING: Mac address to rea
    :return:
    """
    from scapy.all import IP, TCP, sr, sr1

    # 定义目标IP地址范围（使用CIDR表示法）
    target_ip_range = "192.168.2.0/24"

    # 定义目标端口范围
    start_port = 443
    end_port = 443

    # 发送TCP SYN包并接收响应
    for target_ip in ipaddress.ip_network(target_ip_range):
        for port in range(start_port, end_port + 1):
            packet = IP(dst=str(target_ip)) / TCP(dport=port, flags="S")
            response = sr1(packet, timeout=1, verbose=False)
            if response:
                if response.haslayer(TCP) and response.getlayer(TCP).flags == "SA":
                    print(f'存活主机 {target_ip}:{port}')


def udp_request_t():
    from scapy.all import IP, UDP, sr1

    # 定义目标IP地址范围（使用CIDR表示法）
    target_ip_range = "192.168.2.0/24"

    # 定义目标端口范围
    start_port = 1
    end_port = 100

    # 发送UDP数据包并接收响应
    for target_ip in ipaddress.ip_network(target_ip_range):
        for port in range(start_port, end_port + 1):
            packet = IP(dst=str(target_ip)) / UDP(dport=port)
            response = sr1(packet, timeout=1, verbose=False)
            if response:
                if response.haslayer(UDP):
                    print(f'存活主机 {target_ip}:{port}')


if __name__ == '__main__':
    arp_request_t()
    # ping_request_t()
    # tcp_syn_request_t()
    # udp_request_t()
