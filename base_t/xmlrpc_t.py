import sys
import time

if sys.argv[1] == 'server':
    # from xmlrpc.server import SimpleXMLRPCServer
    # from socketserver import ThreadingMixIn
    #
    # class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    #     pass
    #
    # # A marshalling error is going to occur because we're returning a
    # # complex number
    # def myfunc():
    #     r = []
    #     for i in range(10):
    #         r.append(i)
    #         time.sleep(0.1)
    #     print(f"len(r) {len(r)}")
    #     return r
    #
    # # server = SimpleXMLRPCServer(("127.0.0.1", 8000))
    # server = ThreadXMLRPCServer(('127.0.0.1', 8000), allow_none=True)
    # print("Listening on port 8000...")
    # server.register_function(myfunc, 'myfunc')
    #
    # server.serve_forever()

    from socketserver import ThreadingMixIn
    from xmlrpc.server import SimpleXMLRPCServer

    class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
        pass


    # A marshalling error is going to occur because we're returning a
    # complex number
    def add(x, y):
        return x + y


    server = ThreadXMLRPCServer(("localhost", 8000))
    print("Listening on port 8000...")
    server.register_function(add, 'add')

    server.serve_forever()
else:
    # from xmlrpc.client import ServerProxy
    # import threading
    #
    # class MsgXmlRpc:
    #     def __init__(self) -> None:
    #         self.server = None
    #         self.serverurl = "http://127.0.0.1:8000"
    #         self.initServer()
    #         self.ip_online = []
    #         self.start()
    #
    #     def initServer(self):
    #         try:
    #             self.server = ServerProxy(self.serverurl)
    #         except Exception as exp:
    #             print('probe MSG RPC 服务失败', exp)
    #             time.sleep(60)
    #             self.initServer()
    #
    #     def thread_sync_online(self):
    #         while True:
    #             print("running...")
    #             ip_list = self.server.myfunc()
    #             print(f"running len {len(ip_list)}")
    #             self.ip_online = ip_list
    #             time.sleep(30)
    #
    #     def select_ip_online(self, ip):
    #         if ip in self.ip_online:
    #             return True
    #         else:
    #             return False
    #
    #     def get_online_ip(self):
    #         ip_list = self.server.myfunc()
    #         self.ip_online = ip_list
    #         return self.ip_online
    #
    #     def start(self):
    #         # pass
    #         thr = threading.Thread(target=self.thread_sync_online)
    #         thr.start()
    #
    # msg_rpc = MsgXmlRpc()
    # while True:
    #     print("outer running")
    #     res = msg_rpc.get_online_ip()
    #     print(f"outer running {len(res)}")
    #     time.sleep(3 * 60)
    import xmlrpc.client
    import threading

    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    try:
        def thread_sync():
            # p = xmlrpc.client.ServerProxy("http://localhost:8000/")
            while True:
                r = proxy.add(5, 5)
                print(r)
                time.sleep(5)
        thr = threading.Thread(target=thread_sync)
        thr.start()

        # proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
        while True:
            res = proxy.add(2, 5)
            print(res)
            time.sleep(10)
    except xmlrpc.client.Fault as err:
        print("A fault occurred")
        print("Fault code: %d" % err.faultCode)
        print("Fault string: %s" % err.faultString)
