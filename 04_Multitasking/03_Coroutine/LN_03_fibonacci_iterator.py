from collections.abc import Iterable
from collections.abc import Iterator

class Fibonacci(object):

        def __init__(self, num):
                self.num = num
                self.count = 0
                self.a = 0
                self.b = 1

        def __iter__(self):
                return self

        def __next__(self):
                if self.count < self.num:
                        temp = self.a
                        self.a, self.b = self.b, self.a+ self.b
                        self.count += 1
                        return temp
                else:
                        raise StopIteration



fibo = Fibonacci(10)

for num in fibo:
        print(num)


