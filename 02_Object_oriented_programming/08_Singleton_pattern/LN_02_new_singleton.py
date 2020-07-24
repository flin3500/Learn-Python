class MusicPlayer(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        # 1. if instance is None, allocate address
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        # 2. return to init
        return cls.instance

    def __init__(self):
        print("Create music player")


# 1. make object
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)