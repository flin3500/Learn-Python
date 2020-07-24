class A(object):

    def test(self):
        print("A---test")

    def demo(self):
        print("A---demo")


class B(object):

    def demo(self):
        print("B---demo")

    def test(self):
        print("B---test")


class C(A, B):
    pass


c = C()
c.test()
c.demo()

print(C.__mro__)
