class Cat:

    def __init__(self):
        self.name = "Tom"

    def eat(self):
        print("%s eats fish" % self.name)

    def drink(self):
        print("%s drinks water" % self.name)


# when the object made, init automatically run
tom = Cat()

print(tom.name)
