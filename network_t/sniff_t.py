"""
抓包
"""
from scapy.all import *


def my_callback(packet):
    print("begin-------------------------------")
    # print(f"source {packet[IP].src} {packet[IP].sport} dst {packet[IP].dst} {packet[IP].dport}")
    print(packet.show())
    print("end-------------------------------")


if __name__ == '__main__':
    my_filter = "dst 47.116.71.190"
    packets = sniff(filter=my_filter, prn=my_callback, count=5)
    wrpcap("data.pcap", packets)
