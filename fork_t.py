# 僵尸进程  ps -ef | grep defunct
import subprocess
import time
import signal


def fork_t():
    cmd = ["python", "-h"]
    subprocess.Popen(cmd)


if __name__ == "__main__":
    signal.signal(signal.SIGCHLD, signal.SIGINT)   # 没有SIGCHLD？
    fork_t()
    while True:
        time.sleep(5)
