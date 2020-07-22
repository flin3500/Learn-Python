import random
player = int(input("What is your choice? Rock for 1, Paper 2,Scissors 3"))
computer = random.randint(1, 3)
print("Computer chooses {}, player choose {}".format(computer, player))
if ((player == 1 and computer == 3)
        or (player == 2 and computer == 1)
        or (player == 3 and computer == 2)):
    print("you wins")
elif player == computer:
    print("draw")
else:
    print("computer wins")
