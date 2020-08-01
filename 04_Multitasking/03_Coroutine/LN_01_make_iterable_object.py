from collections.abc import Iterable
from collections.abc import Iterator
import time

class Classmate(object):

        def __init__(self):
                self.names = list()

        def add(self, name):
                self.names.append(name)

        # to make the object craete by this class iterable
        def __iter__(self):
                return ClassIterator(self.names)

# Iterator
class ClassIterator(object):

        def __init__(self, names):
                self.names = names
                self.counter = 0

        def __iter__(self):
                pass

        def __next__(self):
                if self.counter < len(self.names):
                        temp = self.names[self.counter]
                        self.counter += 1
                        return temp
                else:
                        raise StopIteration


classmate = Classmate()
classmate.add("Jasmine")
classmate.add("Jane")
classmate.add("Lin")

# print("Justify if classmate is an object which can Iterate: ", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print("Justify if classmate_iterator is an Iterator: ", isinstance(classmate_iterator, Iterator))


for name in classmate:
        print(name)
        time.sleep(1)