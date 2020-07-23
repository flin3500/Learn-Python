class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __str__(self):
        return "I am %s" % self.name
        # change print(object)


tom = Cat("Tom")
print(tom)


