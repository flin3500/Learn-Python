fruit = {"apple": 1,
         "banana": 2,
         "pear": 3}

print(fruit)

# get
print(fruit["apple"])

# change
fruit["apple"] = 18
print(fruit)

# add
fruit["watermelon"] = 4
print(fruit)

# remove
fruit.pop("apple")
print(fruit)

# length
print(len(fruit))

# merge
temp_dict = {"plum": 1.75}
fruit.update(temp_dict)
print(fruit)

# clear
fruit.clear()
print(fruit)




