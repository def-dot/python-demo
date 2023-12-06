"""
IO多路复用
"""
import select
import sys
import socket
import threading


def run_server():
    host = 'localhost'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    client_sockets = [server_socket]

    while True:
        r_list, _, _ = select.select(client_sockets, [], [])
        for sock in r_list:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                client_sockets.append(client_socket)
            else:
                data = sock.recv(1024)
                if data:
                    print("Received data:", data.decode())
                    response = b"HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello, World!"
                    sock.sendall(response)
                else:
                    sock.close()
                    client_sockets.remove(sock)

    server_socket.close()


def run_client():
    host = 'localhost'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = "Hello"
    data = message.encode()
    client_socket.sendall(data)

    response = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(1):
            t = threading.Thread(target=run_client)
            t.start()
    else:
        run_server()
