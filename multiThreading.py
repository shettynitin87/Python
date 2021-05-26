import threading as thread

def print_square(requiredNumber):
    print("Square:{}".format(requiredNumber * requiredNumber))

def print_cube(requiredNumber):
    print("Cube:{}".format(requiredNumber * requiredNumber * requiredNumber))

if __name__ == '__main__':
    #Creating Thread

    thread_1 = thread.Thread(target=print_square,args=(10,))
    thread_2 = thread.Thread(target=print_cube,args=(10,))

    #Initiate the threads
    thread_1.start()
    thread_2.start()

    #Wait till both the threads are completelty executed
    thread_1.join()
    thread_2.join()

    print("Done!!")