import time


if __name__ == '__main__':
    try:
        print('hello world')
    except Exception as e:
        print(str(e))
    while True:
        time.sleep(30)
