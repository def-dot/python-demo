# 计算密集型,同步/异步差别不大,同步甚至更快
# IO密集型,异步远快于同步
import asyncio
import datetime
import random
import time
import sys

from common import cost


@cost
def sync_t():
    def foo(i):
        time.sleep(0.01)
        return 1

    res = 0
    for i in range(100):
        res += foo(i)
    print("cpu_sync_t res %s" % res)


@cost
def async_t():
    async def foo(i):
        await asyncio.sleep(0.01)
        return 1

    async def run():
        tasks = [foo(i) for i in range(100)]  # coroutine object list
        done, pending = await asyncio.wait(tasks)  # done和pending是set类型,元素为Task(Future子类)
        res = 0
        for i in done:
            res += i.result()
        print("cpu_async_t res %s" % res)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


@cost
def async_gather_t():
    # gather和wait都会阻塞,直到所有task都完成
    # gather按tasks顺序返回
    # gather直接返回运行结果(asyncio.gather是future类型,为什么能直接打印运行结果?)
    async def foo1():
        await asyncio.sleep(1)
        print("2S")
        await asyncio.sleep(2)
        return 2

    async def foo2():
        print("5S")
        await asyncio.sleep(5)
        return 5

    async def run():
        tasks = [foo2(), foo1()]  # coroutine object list
        f = await asyncio.gather(*tasks)
        for i in f:
            print(i)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


@cost
def done_t():
    # wait会阻塞,直到所有task都完成
    # wait返回结果是无序的(相对执行顺序)
    async def foo1():
        await asyncio.sleep(1)
        print("2S")
        await asyncio.sleep(2)
        return 2

    async def foo2():
        print("5S")
        await asyncio.sleep(5)
        return 5

    async def run():
        tasks = [foo2(), foo1()]  # coroutine object list
        done, pending = await asyncio.wait(tasks)  # done和pending是set类型,元素为Task(Future子类)
        res = 0
        for i in done:
            print(i.result())
        print("done_t res %s" % res)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


def await_sync_t():
    async def sleep_t():
        # await 接同步代码测试
        time.sleep(1)
        print("over")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(sleep_t())


def queue_t():
    async def work(i, queue):
        while True:
            v = await queue.get()
            await asyncio.sleep(v)
            queue.task_done()
            print(f"worker {i} sleep {v}")

    async def main():
        queue = asyncio.Queue()
        # 100个消息
        for i in range(100):
            sleep_time = random.uniform(0.1, 1)
            queue.put_nowait(sleep_time)

        # 三个消费者
        tasks = []
        t = asyncio.create_task(work(1, queue))
        tasks.append(t)
        t = asyncio.create_task(work(2, queue))
        tasks.append(t)
        t = asyncio.create_task(work(3, queue))
        tasks.append(t)

        start_time = time.monotonic()
        await queue.join()
        end_time = time.monotonic()
        print(f"cost {end_time-start_time}")

        for t in tasks:
            t.cancel()

    asyncio.run(main())


def subprocess_shell_t():
    async def run(cmd):
        proc = await asyncio.create_subprocess_shell(cmd,
                                                     stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await proc.communicate()
        if stdout:
            print(f"stdout {stdout}")
        if stderr:
            print(f"stderr {stderr}")

    async def main():
        await asyncio.gather(
            run('python async_t.py client'),
        )

    asyncio.run(main())


def subprocess_exec_t():
    async def main():
        proc = await asyncio.create_subprocess_exec('ping', 'www.baidu.com',
                                                    stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        res = await proc.stdout.readline()
        print(f"res {res}")
        await proc.wait()

    asyncio.run(main())


def stream_client_t(msg):
    # async def tcp_client():
    #     print("tcp_client")
    #     reader, writer = await asyncio.open_connection(host="127.0.0.1", port=8888)
    #     # send
    #     msg = "hello"
    #     writer.write(msg.encode())
    #     await writer.drain()
    #     print(f"client write {msg}")
    #     # recv
    #     res = await reader.read()
    #     print(f"client read {res}")
    #
    #     writer.close()
    #     await writer.wait_closed()
    #
    # asyncio.run(tcp_client())

    async def tcp_echo_client(message):
        reader, writer = await asyncio.open_connection(
            '127.0.0.1', 8888)

        print(f'Send: {message!r}')
        writer.write(message.encode())
        await writer.drain()

        # data = await reader.read(100)
        # print(f'Received: {data.decode()!r}')

        print('Close the connection')
        writer.close()
        await writer.wait_closed()

    asyncio.run(tcp_echo_client(msg))


def stream_server_t():
    # async def handle_client(reader, writer):
    #     print(f"handle_client")
    #     res = await reader.read()
    #     print(f"server read {res}")
    #     msg = "reply " + res.decode()
    #     print(f"server {msg}")
    #     writer.write(msg.encode())
    #     await writer.drain()
    #
    #     writer.close()
    #     await writer.wait_closed()
    #
    # async def tcp_server():
    #     server = await asyncio.start_server(handle_client, host="127.0.0.1", port=8888)
    #     print(f"start_server")
    #     async with server:
    #         await server.serve_forever()
    #
    # asyncio.run(tcp_server())

    async def handle_echo(reader, writer):
        time.sleep(5)
        print(f"handle_echo begin---- {datetime.datetime.now()}")
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received {message!r} from {addr!r}")

        print(f"Send: {message!r}")
        writer.write("reply".encode())
        await writer.drain()

        print("Close the connection")
        writer.close()
        await writer.wait_closed()

    async def main():
        server = await asyncio.start_server(
            handle_echo, '127.0.0.1', 8888)

        addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
        print(f'Serving on {addrs}')

        async with server:
            await server.serve_forever()

    asyncio.run(main())


if __name__ == '__main__':
    # sync_t()  # 155.41
    # async_t()  # 0.15
    # done_t()
    # async_gather_t()
    # await_sync_t()
    # queue_t()
    # subprocess_shell_t()
    # subprocess_exec_t()
    if sys.argv[1] == "client":
        stream_client_t("hello world")
        stream_client_t("how are you")
    else:
        stream_server_t()
