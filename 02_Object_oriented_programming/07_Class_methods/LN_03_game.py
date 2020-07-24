class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def help():
        print("Kill all enemies")

    @classmethod
    def show_top_score(cls):
        print("Top score is %d" % cls.top_score)

    def start_game(self):
        print("GAME BEGIN")


# 1. SEE HELP
Game.help()
# 2. SEE TOP
Game.show_top_score()
# 3. CREATE PLAYER
tom = Game("Tom")
tom.start_game()
