from multiprocessing import Pool
import os, time, random

def worker(msg):
        t_start = time.time()
        print("%s start, pid is %d" % (msg,os.getpid()))
        time.sleep(random.random()*2) 
        t_stop = time.time()
        print(msg,"Finish，spend %0.2f" % (t_stop-t_start))

def main():
        po = Pool(3)  # max 3 process
        for i in range(0,10):
                po.apply_async(worker,(i,))
        print("----start----")
        po.close()  
        po.join()  
        print("-----end-----")

if __name__ == "__main__":
        main()