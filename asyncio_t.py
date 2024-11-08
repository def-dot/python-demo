import asyncio

# 异步处理客户端连接的函数
async def handle_client(reader, writer):
    data = await reader.read(100)  # 等待并读取数据
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message} from {addr}")

    response = f"Hello {addr}!"
    writer.write(response.encode())  # 发送响应
    await writer.drain()  # 确保数据已经发送

    print("Close the connection")
    writer.close()  # 关闭连接
    await writer.wait_closed()  # 等待连接关闭

# 主协程，用于启动服务器
async def main():
    # 创建并启动服务器，监听指定地址和端口
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    # 使用异步上下文管理器启动服务器
    async with server:
        await server.serve_forever()  # 服务器将永远运行，直到被手动停止

# 获取事件循环并运行主协程
asyncio.run(main())
