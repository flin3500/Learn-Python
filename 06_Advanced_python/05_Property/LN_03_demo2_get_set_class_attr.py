class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error: not an integer")

    money = property(getMoney, setMoney)  

a = Money()
a.money = 100
print(a.money)