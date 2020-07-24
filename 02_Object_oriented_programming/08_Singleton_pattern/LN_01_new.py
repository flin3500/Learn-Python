class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 1. allocate address
        instance = super().__new__(cls)
        # 2. return to init
        return instance

    def __init__(self):
        print("Create music player")


# 1. make object
player = MusicPlayer()
print(player)