intro = ["\t\nhi",
         "I\t\n",
         "am",
         "lin"]

for i in intro:
    print(i.strip(), end="")
    print(i.strip().center(20), end="")
    print(i.strip().rjust(1))
