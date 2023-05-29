import IPy

i = "172.16.0.0/16"
len_ip = IPy.IP(i, make_net=1).len()
# if '/8' in i:
#     len_ip = len_ip - (256 * 256 * 2)
# elif '/16' in i:
#     len_ip = len_ip - (256 * 2)
# elif '/24' in i:
#     len_ip = len_ip - 2
print(len_ip)