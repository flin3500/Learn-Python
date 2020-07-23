class Cat:

    def eat(self):
        print("Cat eats fish")

    def drink(self):
        print("Cat drinks water")


tom = Cat()
tom.eat()
tom.drink()

print(tom)
# <__main__.Cat object at 0x1015124e0>
#           Class         address

print("%x" % id(tom))
