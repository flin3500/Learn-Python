from LN_01_mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId
import math
import datetime

db = client.school
gfs = GridFS(db, collection="book")
book = gfs.find_one({"filename":"how_to_learn_linux.pdf"})
print(book.filename)
print(book.type)
print(book.keyword)
print(math.ceil(book.length/1024/1024))


print("----------------------")

books = gfs.find({"type":"PDF"})
for one in books:
	uploadDate = one.uploadDate + datetime.timedelta(hours=10)
	uploadDate = uploadDate.strftime("%Y-%m-%d %H:%M:%S")
	print(one._id, one.filename, uploadDate)

print("----------------------")

rs = gfs.exists(ObjectId("5f361d200ec309923ed8e666"))
print(rs)
rs = gfs.exists(**{"type":"PDF"})
print(rs)