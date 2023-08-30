from scapy.config import conf
from scapy.all import *


class ScapyT:
    def config_t(self):
        print(conf)

    def ip_t(self):
        # 构造IP包
        IP(ttl=10, dst='172.16.30.32')
        s = IP(dst='www.baidu.com')/ICMP()
        s.show()
        sniff(timeout=10)


if __name__ == '__main__':
    s = ScapyT()
    # s.config_t()
    s.ip_t()
