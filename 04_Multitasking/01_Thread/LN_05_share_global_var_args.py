import threading
import time

def test1(temp):
        temp.append(33)
        print("test1: %s" % str(temp))

def test2(temp):
        print("test1: %s" % str(temp))

nums = [11, 22]

def main():
        t1 = threading.Thread(target=test1, args=(nums,))
        t2 = threading.Thread(target=test2, args=(nums,))

        t1.start()
        time.sleep(1)

        t2.start()
        time.sleep(1)

        print("main: %s" % str(nums))

if __name__ == "__main__":
        main()