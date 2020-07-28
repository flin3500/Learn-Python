import threading
import time

num = 100

def test1():
        global num
        num +=1
        print("test1: %d" % num)

def test2():
        print("test2: %d" % num)

def main():
        t1 = threading.Thread(target=test1)
        t2 = threading.Thread(target=test2)
        t1.start()
        time.sleep(1)
        t2.start()
        time.sleep(1)
        print("main: %d" % num)


if __name__ == "__main__":
        main()