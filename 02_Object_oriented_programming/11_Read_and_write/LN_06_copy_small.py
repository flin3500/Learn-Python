# 1. open file
file_read = open("README")
file_write = open("README[COPY1]","w")
# 2. read and write
text = file_read.read()
file_write.write(text)
# 3. close
file_read.close()
file_write.close()
