from ctypes import *
from threading import Thread

# load library
lib = cdll.LoadLibrary("./libdead_loop.so")

# make a thread and do the function in library
t = Thread(target=lib.DeadLoop)
t.start()

# main thread
while True:
    pass
