from helloworld_pb2 import helloworld

if __name__ == '__main__':
    hw = helloworld()

    with open('mybuffer.io', 'rb') as f:
        hw.ParseFromString(f.read())
        print(hw)
