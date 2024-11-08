import subprocess
import time


if __name__ == "__main__":
    process =subprocess.Popen(
                ["python", "add_t.py", "1", "2"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
    # stdout, stderr = process.communicate()
    # print(stdout.decode("utf-8"))
    print("over")
