"""
广播测试
"""
import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    message = "hello world"
    try:
        sent_bytes = sock.sendto(message.encode('utf-8'), ('172.16.255.255', 8888))
        print(f"broadcast success {sent_bytes}")
    except Exception as e:
        print(f"broadcast error： {str(e)}")
    finally:
        sock.close()


if __name__ == '__main__':
    main()
