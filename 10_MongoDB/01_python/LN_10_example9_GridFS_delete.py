from LN_01_mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId
import os

db = client.school
gfs = GridFS(db, collection="book")

gfs.delete(ObjectId("5f361d200ec309923ed8e666"))