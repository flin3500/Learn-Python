import random  # if we have another file named random.py, this file will cause error
print(random.__file__)
rand = random.randint(0, 10)
print(rand)
