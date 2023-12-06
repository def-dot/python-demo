from scapy.all import *
import socket


def get_dns_analysis(url):
    target_ip = socket.gethostbyname(url)
    return target_ip


def http_request_t():
    target_ip = get_dns_analysis("www.example.com")
    print(f"target_ip {target_ip}")
    # 构建HTTP GET请求报文
    http_request = Ether() / IP(dst=target_ip) / TCP(dport=80) / Raw(b"GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n")

    # 发送请求并接收响应
    http_response = srp1(http_request)

    # 打印响应内容
    print(http_response.show())


if __name__ == '__main__':
    http_request_t()
