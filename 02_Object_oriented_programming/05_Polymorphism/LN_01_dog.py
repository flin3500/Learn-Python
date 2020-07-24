class Dog(object):

    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s is playing" % self.name)


class FlyingDog(Dog):

    def play(self):
        print("%s is flying and playing" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s and %s are playing together" % (self.name, dog.name))
        dog.play()


lucky = FlyingDog("Lucky")
lin = Person("Lin")
lin.play_with_dog(lucky)
