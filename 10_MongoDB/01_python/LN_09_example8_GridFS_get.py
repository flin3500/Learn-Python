from LN_01_mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId
import os

db = client.school
gfs = GridFS(db, collection="book")

document = gfs.get(ObjectId("5f361d200ec309923ed8e666"))
book = os.path.expanduser('~/Desktop/how_to_learn_linux1.pdf')
file = open(book, "wb")
file.write(document.read())
file.close()