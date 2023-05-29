from xmlrpc.client import ServerProxy

if __name__ == "__main__":
    server = ServerProxy("http://localhost:8888")
    res = server.func1("sjj")
    print(res)

