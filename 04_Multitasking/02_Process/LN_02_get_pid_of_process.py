import multiprocessing
import os
import time


def test():
    while True:
        print("----in child process pid=%d , parent process pid=%d---" % (os.getpid(), os.getppid()))
        time.sleep(1)


def main():
    print("----in main process pid=%d---parent process pid=%d----" % (os.getpid(), os.getppid()))
    p = multiprocessing.Process(target=test)
    while True:
        continue
    p.start()


if __name__ == "__main__":
    main()
