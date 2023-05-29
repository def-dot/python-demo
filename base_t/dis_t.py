import dis

# n = 0


# def foo():
#     global n
#     n += 1


lst = [4, 1, 3, 2]


def foo():
    lst.sort()


dis.dis(foo)
