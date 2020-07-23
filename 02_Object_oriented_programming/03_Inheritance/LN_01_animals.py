class Animals:

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animals):

    def bark(self):
        print("bark")


class FlyingDog(Dog):

    def fly(self):
        print("fly")

    def bark(self):
        print("Wow")
        super().bark()  # Python 3.x recommend
        Dog.bark(self)  # Python 2.x


dog = FlyingDog()
dog.bark()
