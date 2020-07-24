# 1. open file
file_read = open("README")
file_write = open("README[COPY2]","w")
# 2. read and write
while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)
# 3. close
file_read.close()
file_write.close()
