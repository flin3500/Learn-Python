def demo1():
    return int(input("Input number: "))


def demo2():
    return demo1()


try:
    print(demo2())
except Exception as result:
    print("Error: %s" % result)
