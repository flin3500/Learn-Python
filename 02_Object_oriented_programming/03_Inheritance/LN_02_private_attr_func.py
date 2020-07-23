class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("private func %d %d" % (self.num1, self.__num2))


class B(A):

    def demo(self):
        # print("private attr %d" % self.__num2) # can not
        # self.__test                            # can not
        pass

b = B()
b.demo()
