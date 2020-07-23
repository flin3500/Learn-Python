class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "My name is %s, weight is %s" % (self.name, self.weight)

    def run(self):
        print("%s likes running" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s likes eating" % self.name)
        self.weight += 1


jerry = Person("Jerry", 75.0)
jerry.run()
jerry.eat()
print(jerry)

print()

lin = Person("Lin", 90.0)
lin.run()
lin.eat()
print(lin)
