def generate(num):
    while num > 0:
        num = num - 1
        yield num

g = generate(10)
for i in g:
    print(i)
