import os
import re
import time
import asyncio
import subprocess
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from scapy.all import *
from scapy.supersocket import L3RawSocket



def asyncGetPing(ip_s: list):
    for ip in ip_s:
        raw_socket = L3RawSocket()
        icmp_pack = IP(dst=ip) / ICMP()
        raw_socket.send(icmp_pack)

def cmd_t(ip):
    pingCmd = "ping -c 1 -w 1 {}".format(ip)
    res_obj = os.popen(pingCmd)
    content = res_obj.read()
    ttl = re.search("ttl=(.*?) ", content)
    if ttl:
        return ttl.group(1)
    else:
        return None


async def async_cmd_t(ip):
    pingCmd = "ping -c 1 -w 1 {}".format(ip)
    res_obj = await asyncio.create_subprocess_shell(
        pingCmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE
    )
    stdout, stderr = await res_obj.communicate()
    content = stdout.decode('utf-8')
    ttl = re.search("ttl=(.*?) ", content)
    if ttl:
        return ttl.group(1)
    else:
        return None


async def async_t(ips):
    tasks = []
    time1 = time.time()
    for ip in ips:
        tasks.append(async_cmd_t(ip))
    await asyncio.gather(*tasks)
    time2 = time.time()
    print("async cost %s" % (time2 - time1))


def thread_t(ips):
    executor = ThreadPoolExecutor(max_workers=20)
    tasks = []
    time1 = time.time()
    for ip in ips:
        tasks.append(executor.submit(cmd_t, (ip)))
    wait(tasks, return_when=ALL_COMPLETED)
    time2 = time.time()
    print("thread cost %s" % (time2 - time1))


def subprocess_t(ips):
    for ip in ips:
        result = subprocess.call('ping -c 1 -w 1 %s' % ip, shell=True, stdout=subprocess.PIPE)
        # if result == 0:
        #     print("up")
        # else:
        #     print("down")


if __name__ == '__main__':
    ips = ['172.16.0.1'] * 100
    time1 = time.time()
    # thread_t(ips)
    # subprocess_t(ips)
    # asyncio.run(async_t(ips))
    asyncGetPing(ips)
    time2 = time.time()
    print("cost %s" % (time2 - time1))
