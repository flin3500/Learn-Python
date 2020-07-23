class Cat:

    def __init__(self, new_name):
        self.name = new_name

    def eat(self):
        print("%s eats fish" % self.name)

    def drink(self):
        print("%s drinks water" % self.name)


tom = Cat("Tom")
garfield = Cat("Garfield")

print(tom.name)
print(garfield.name)
