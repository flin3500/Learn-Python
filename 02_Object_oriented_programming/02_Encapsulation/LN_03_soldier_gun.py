class Gun:

    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count;

    def shoot(self):
        if self.bullet_count <= 0:
            print("No bullet in [%s]" % self.model)
            return
        self.bullet_count -= 1
        print("BAM!...[%d]" % self.bullet_count)


class Soldier:

    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("%s do not have gun." % self.name)
            return
        print("%s: Go !!!!" % self.name)
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("AK47")
Jack = Soldier("Jack")
Jack.gun = ak47
Jack.fire()


