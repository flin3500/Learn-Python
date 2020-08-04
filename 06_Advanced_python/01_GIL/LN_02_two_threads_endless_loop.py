import threading

# child thread endless
def test():
    while True:
        pass


t1 = threading.Thread(target=test)
t1.start()

# main thread endless
while True:
    pass
