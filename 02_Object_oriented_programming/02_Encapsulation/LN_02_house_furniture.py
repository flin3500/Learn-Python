class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] needs %.2f" % (self.name, self.area)


class LivingPlace:
    def __init__(self, type, area):
        self.type = type
        self.area = area
        self.remain_area = area
        self.item_list = []

    def __str__(self):
        return ("Type: %s\nArea: %.2f[Remain: %.2f]\nFurniture: %s"
                % (self.type, self.area, self.remain_area, self.item_list))

    def add_item(self, item):
        if item.area > self.remain_area:
            print("%s is too big, cannot place in" % item.name)
            return
        self.item_list.append(item.name)
        self.remain_area -= item.area


bed = Furniture("Queen size bed", 4)
closet = Furniture("Closet", 2)
table = Furniture("Table", 1.5)
# print(bed)
# print(closet)
# print(table)

my_home = LivingPlace("Apartment", 120)
my_home.add_item(bed)
my_home.add_item(closet)
my_home.add_item(table)

print(my_home)
