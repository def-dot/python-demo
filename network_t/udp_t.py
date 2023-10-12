import socket

# 创建UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器地址和端口
server_address = ('156.232.11.125', 12345)

# 发送数据到服务器
message = 'Hello, server!'
sock.sendto(message.encode(), server_address)

# 接收服务器的响应
data, address = sock.recvfrom(1024)  # 一次最多接收1024字节的数据
print('接收到来自', address, '的响应:', data.decode())

# 关闭socket连接
sock.close()
