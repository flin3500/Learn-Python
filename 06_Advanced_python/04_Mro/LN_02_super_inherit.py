class Parent(object):
    def __init__(self, name, *args, **kwargs): 
        print('parent init start')
        self.name = name
        print('parent init finish')

class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs): 
        print('Son1 init start')
        self.age = age
        super().__init__(name, *args, **kwargs)  
        print('Son1 init finish')

class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('Son2 init start')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('Son2 init finish')

class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        print('Grandson init start')
        super().__init__(name, age, gender)
        print('Grandson init finish')

print(Grandson.__mro__)

gs = Grandson('grandson', 12, 'male')
print('Name：', gs.name)
print('Age：', gs.age)
print('Gender：', gs.gender)