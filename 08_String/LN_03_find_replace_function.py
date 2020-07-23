hello_str="hello world"

# start
print(hello_str.startswith("h"))

# end
print(hello_str.endswith("d"))

# find(index function will cause error if can not find)
print(hello_str.find("w"))
print(hello_str.find("abc"))

# replace(can not change original one)
print(hello_str.replace("world", "python"))
print(hello_str)
