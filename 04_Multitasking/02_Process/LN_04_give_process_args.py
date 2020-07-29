import multiprocessing
import os
import time


def test(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


def main():
    print("----in main process pid=%d---parent process pid=%d----" % (os.getpid(), os.getppid()))
    p = multiprocessing.Process(target=test, args=(11, 22, 33, 44, 55, 66, 77, 88), kwargs={"mm":11})
    p.start()


if __name__ == "__main__":
    main()
