i = 1
while i <= 9:
    y = 1
    while y <= i:
        print("{} * {} = {}".format(y, i, i*y), end="\t")
        y += 1
    i += 1
    print("")
