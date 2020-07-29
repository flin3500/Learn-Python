import multiprocessing
import os
import time


nums = [11, 22, 33]


def test():
    nums.append(44)
    print("In process 1: nums=%s" % str(nums))
    time.sleep(3)


def test2():
    print("In process 2: nums=%s" % str(nums))


def main():
    print("----in main process: pid=%d---in parent process pid=%d----" % (os.getpid(), os.getppid()))
    p = multiprocessing.Process(target=test)
    p.start()

    # time.sleep(1)
    p.join()

    p2 = multiprocessing.Process(target=test2)
    p2.start()

if __name__ == "__main__":
    main()
