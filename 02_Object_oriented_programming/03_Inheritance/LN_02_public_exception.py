class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("private func %d %d" % (self.num1, self.__num2))

    def test(self):
        print("public function %d" % self.__num2)
        self.__test()


class B(A):

    def demo(self):
        # print("private attr %d" % self.__num2) # can not
        # self.__test                            # can not
        # print(self.num1)                       # can
        self.test()                            # can


b = B()
b.demo()
