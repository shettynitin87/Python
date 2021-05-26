import os
import threading as thread


def task1():
    print("Task 1 assigned to following thread {}".format(thread.current_thread().name))
    print("ID of process running task 1 {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to following thread {}".format(thread.current_thread().name))
    print("ID of process running task 2 {}".format(os.getpid()))


if __name__ == '__main__':
    # Print ID of the current process
    print("ID of process running main program {}".format(os.getppid()))

    # Print name of main thread
    print("The name of the main thread {}".format(thread.current_thread().name))

    # Creating Threads
    thread_1 = thread.Thread(target=task1, name='thread_1')
    thread_2 = thread.Thread(target=task2, name='thread_2')

    # Initiate the threads
    thread_1.start()
    thread_2.start()

    # Wait till both the threads are completed
    thread_1.join()
    thread_2.join()
