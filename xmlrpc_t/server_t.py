from xmlrpc.server import SimpleXMLRPCServer


def get_string(val):
    return "get string" + val


if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8888))
    server.register_function(get_string, "func1")
    server.serve_forever()
