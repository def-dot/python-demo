def test():
    try:
        return 1
    finally:
        print("finally")


r = test()
print(r)
