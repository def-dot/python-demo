def fib(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        c = a + b
        yield c
        a = b
        b = c
        i = i + 1


for item in fib(10):
    print(item)
