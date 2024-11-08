"""
非阻塞IO
"""
import sys
import socket
import threading
import time


def run_server():
    host = 'localhost'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    server_socket.setblocking(False)

    client_sockets = []

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            client_socket.setblocking(False)
            client_sockets.append(client_socket)
            print("New connection:", client_address)
        except BlockingIOError as e:
            pass

        for sock in client_sockets:
            try:
                data = sock.recv(1024)
                if data:
                    print("Received data:", data.decode())
                    response = b"HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello, World!"
                    sock.sendall(response)
            except BlockingIOError as e:
                pass
            except ConnectionResetError as e:
                sock.close()
                client_sockets.remove(sock)

    server_socket.close()


def run_client():
    host = 'localhost'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.setblocking(False)

    try:
        client_socket.connect((host, port))
    except BlockingIOError as e:
        pass

    message = "Hello"
    sys.getsizeof(message)
    data = message.encode()

    while True:
        try:
            if data:
                sent_bytes = client_socket.send(data)
                data = data[sent_bytes:]
            else:
                break
        except BlockingIOError as e:
            pass

    while True:
        try:
            response = client_socket.recv(1024)
            if response:
                print("Received response:", response.decode())
            else:
                print("Server closed the connection")
                break
        except BlockingIOError as e:
            pass

    client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(1):
            t = threading.Thread(target=run_client)
            t.start()
    else:
        run_server()
