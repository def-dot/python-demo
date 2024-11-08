import time

while True:
    with open("a.txt", 'r') as file:
        if file.read():
            break
        else:
            time.sleep(1)
