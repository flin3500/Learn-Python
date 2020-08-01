import os
import multiprocessing

def read_copy(q, file_name, original_folder_name, new_folder_name):
        # print("======>Copy file: from %s to %s, filename is %s" % (original_folder_name, new_folder_name, file_name))
        origin_file = open(original_folder_name + "/" + file_name, "rb")
        content = origin_file.read()
        origin_file.close()

        new_file = open(new_folder_name + "/" + file_name, "wb")
        new_file.write(content)
        new_file.close()

        # when finish, add to queue
        q.put(file_name)

def main():
        # 1. get the name of the original folder want to copy
        original_folder_name = input("Input the folder want to copy: ")

        # 2. make a new folder
        try:
                new_folder_name = original_folder_name + "[new]"
                os.mkdir(new_folder_name)
        except:
                pass

        # 3. use listdir() to get all the files name in the original folder
        file_names = os.listdir(original_folder_name)

        # 4. create process pool
        po = multiprocessing.Pool(5)

        # 5. make a queue
        q = multiprocessing.Manager().Queue()

        # 6. give process pool all the copy tasks
        for file_name in file_names:
                po.apply_async(read_copy, args = (q, file_name, original_folder_name, new_folder_name))

        po.close()
        # po.join()
        folder_len = len(file_names)
        copy_complete = 0
        while True:
                file_name = q.get()
                copy_complete+=1
                print("\rProcess Rate: %.2f%%" % (copy_complete/folder_len*100), end = "")
                if copy_complete>= folder_len:
                        break

        print()


if __name__ == "__main__":
        main()