class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):
        print("Tool: %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


ax = Tool("Ax")
sd = Tool("Screwdriver")
Tool.show_tool_count()
