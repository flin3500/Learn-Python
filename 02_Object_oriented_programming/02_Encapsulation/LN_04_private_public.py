class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 18  # private attribute

    def __secret(self):  # private function
        print("%s's age is %d" % (self.name, self.__age))


stephine = Person("Stephine")
# stephine.age
# stephine.__secret()

# still can get the private
print(stephine._Person__age)
stephine._Person__secret()


