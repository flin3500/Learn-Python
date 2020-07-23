class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s is coming" % self.name)

    def __del__(self):
        print("%s is go" % self.name)


# when the object made, init automatically run
tom = Cat("Tom")

# del tom

print("*"*50)

