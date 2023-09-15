import ipaddress

cidr = "192.168.1.1/24"

try:
    network = ipaddress.ip_network(cidr)
    print("CIDR表示法合法")
except ValueError as e:
    print("CIDR表示法不合法")
