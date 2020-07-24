class MusicPlayer(object):

    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. if instance is None, allocate address
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        # 2. return to init
        return cls.instance

    def __init__(self):
        # 1.justify if init_flag is false
        if MusicPlayer.init_flag:
            return
        # 2. if it is false, initiate
        print("Create music player")
        # 3. change flag
        MusicPlayer.init_flag = True


# 1. make object
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
