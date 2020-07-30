import multiprocessing


def download(q):
        """download data"""
        data = [11, 22, 33, 44]

        # put data into queue
        for temp in data:
                q.put(temp)

        print("downloader finish")

def analysis(q):
        """analysis data"""

        container = list()
        # get data from queue
        while True:
                data = q.get()
                container.append(data)
                if q.empty():
                        break

        print(container)
        

def main():
        multiprocessing.set_start_method("fork")
        # 1. create a queue
        q = multiprocessing.Queue()
        # 2. create several processes, pass the queue as argument
        p1 = multiprocessing.Process(target=download, args = (q,))
        p2 = multiprocessing.Process(target=analysis, args = (q,))

        p1.start()
        p2.start()

if __name__ == "__main__":
        main()