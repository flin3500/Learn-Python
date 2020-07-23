class Cat:

    def eat(self):
        print("%s eats fish" % self.name)

    def drink(self):
        print("%s drinks water" % self.name)


tom = Cat()
tom.name = "Tom" # not recommended
tom.eat()
tom.drink()

garfield = Cat()
garfield.name = "Garfield"  # not recommended
garfield.eat()
garfield.drink()

# not the same address
print(tom)  # 0x1102365f8
print(garfield)  # 0x1102365c0

