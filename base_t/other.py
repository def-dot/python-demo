import dis
import configparser
import hashlib
import os.path
import re


def re_t():
    text = ''
    r = re.split('。|!|？', text)[0]
    print(r)


def hashlib_t():
    with open("../suanfa/array_find_once_t.py", "rb") as f:
        content = f.read()
        hash_obj = hashlib.sha256()
        hash_obj.update(content)
        hash_val = hash_obj.hexdigest()
        print(hash_val)
    r = os.path.getsize("../suanfa/array_find_once_t.py")
    print(r)


def dis_t():
    lst = [4, 1, 3, 2]

    def foo():
        lst.sort()
    dis.dis(foo)  # list原子性理解


def configparser_t():
    conf = configparser.ConfigParser()
    conf.read("config.ini", encoding="utf-8")
    r = conf.items("apps_list")
    print(r)


if __name__ == "__main__":
    hashlib_t()
    dis_t()
    configparser_t()
    re_t()
