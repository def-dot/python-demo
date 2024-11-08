import socket

raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
