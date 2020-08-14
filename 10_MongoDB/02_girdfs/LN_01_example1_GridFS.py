from LN_01_mongo_db import client
from gridfs import GridFS
import os

db = client.school
gfs = GridFS(db, collection="book")

book = os.path.expanduser('~/Desktop/how_to_learn_linux.pdf')
file = open(book, "rb")
args = {"type":"PDF","keyword":"linux"}
gfs.put(file ,filename="how_to_learn_linux.pdf", **args)
file.close()


