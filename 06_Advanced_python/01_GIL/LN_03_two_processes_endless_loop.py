import multiprocessing

def deadLoop():
    while True:
        pass

# child process endless
multiprocessing.set_start_method("fork")
p1 = multiprocessing.Process(target=deadLoop)
p1.start()

while True:
	# main process endless
	deadLoop()
