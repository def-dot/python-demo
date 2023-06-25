import IPy


def check_ip(ip):
    try:
        IPy.IP(ip)
    except Exception:
        print(f"not ip error: {ip}")


# net转IP列表
def IPSplitBlocks(ip2ip_str):
    """
    ip范围转换为ip列表，不包括网络号0、广播地址255
    """
    if '/' in ip2ip_str:
        ips = IPy.IP(ip2ip_str, make_net=1)
        ipx = [ips[0].net().strNormal(), ips[-1].net().strNormal()]
    elif '-' in ip2ip_str:
        ipx = ip2ip_str.split('-')
    else:
        # 排查 广播地址 网络号
        if ip2ip_str.endswith('.0') or ip2ip_str.endswith('.255'):
            return []
        return [ip2ip_str]
    ip2num = lambda x: sum([256 ** i * int(j) for i, j in enumerate(x.split('.')[::-1])])
    num2ip = lambda x: '.'.join([str(x // (256 ** i) % 256) for i in range(3, -1, -1)])
    a = [num2ip(i) for i in range(ip2num(ipx[0]), ip2num(ipx[1]) + 1) if not ((i + 1) % 256 == 0 or (i) % 256 == 0)]
    return a


if __name__ == "__main__":
    # check_ip(ip="127.0.0.258")
    r = IPSplitBlocks("172.16.0.0/24")
    print(len(r))
    print(r)
