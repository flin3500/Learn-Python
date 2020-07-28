import threading
import time

num = 0

def test1(count):
        global num
        for i in range(count):
                num +=1
        print("test1: %d" % num)

def test2(count):
        global num
        for i in range(count):
                num +=1
        print("test2: %d" % num)

def main():
        t1 = threading.Thread(target=test1, args=(1000000,))
        t2 = threading.Thread(target=test2, args=(1000000,))
        t1.start()
        t2.start()

        time.sleep(5)
        print("main: %d" % num)

if __name__ == "__main__":
        main()