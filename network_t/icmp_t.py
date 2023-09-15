from scapy.all import *

# 构建ICMP回显请求数据包
packet = IP(dst='192.168.13.236') / ICMP(type=8)

# 发送数据包并接收回复
reply = sr1(packet, timeout=2)

# 解析回复数据包
if reply is not None:
    reply.show()
    print('ICMP回显请求成功')
else:
    print('ICMP回显请求超时')
