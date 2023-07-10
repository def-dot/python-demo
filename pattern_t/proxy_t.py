# 代理模式，代理执行，通过代理进行权限等方面的管控

def main():
    print("doing....")


def proxy(user):
    if user == 'admin':
        main()
    else:
        print("rejected")


if __name__ == '__main__':
    # proxy('admin')
    proxy('zhangsan')
