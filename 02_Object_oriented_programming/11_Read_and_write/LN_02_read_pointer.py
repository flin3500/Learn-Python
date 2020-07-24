# 1. open file
file = open("README")
# 2. read file
text = file.read()
print(text)
print(len(text))
print("-"*50)
text1 = file.read()     # cannot read anything because the pointer already at the end
print(text1)
print(len(text1))

# 3. close file
file.close()
