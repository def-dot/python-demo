from helloworld_pb2 import helloworld

if __name__ == '__main__':
    hw = helloworld()
    hw.id = 123
    hw.str = 'test'
    print(hw)

    with open('mybuffer.io', 'wb') as f:
        f.write(hw.SerializeToString())
