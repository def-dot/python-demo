class Generator:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 0:
            self.num = self.num - 1
            return self.num
        else:
            raise StopIteration
g = Generator(10)
for i in g:
    print(i)
