class Parent(object):
    def __init__(self, name):
        print('parent init start')
        self.name = name
        print('parent init finish')

class Son1(Parent):
    def __init__(self, name, age):
        print('Son1 init start')
        self.age = age
        Parent.__init__(self, name)
        print('Son1 init finish')

class Son2(Parent):
    def __init__(self, name, gender):
        print('Son2 init start')
        self.gender = gender
        Parent.__init__(self, name)
        print('Son2 init finish')

class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson init start')
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print('Grandson init finish')



gs = Grandson('grandson', 12, 'male')
print('Name：', gs.name)
print('Age：', gs.age)
print('Gender：', gs.gender)


# in this way the Parent will run for two times, which is not efficient