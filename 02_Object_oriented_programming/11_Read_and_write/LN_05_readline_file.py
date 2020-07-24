# 1. open file
file = open("README")
# 2. read file
while True:
    text = file.readline()
    if not text:
        break
    print(text)
# 3. close file
file.close()
