def gen():
    while True:
        res = yield 4
        print("res %s" % res)


if __name__ == "__main__":
    g = gen()
    print(g)
    print("next 1-----")
    print(next(g))
    print("next 2-------")
    print(next(g))
    print("next 3-------")
    print(g.send(3))



