class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


ax = Tool("Ax")
sd = Tool("Screwdriver")
print(ax.count)         # use object to get class attribute from ax -> Tool -> Object
print(sd.count)         # use object to get class attribute
