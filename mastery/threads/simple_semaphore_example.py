# importing the modules
from threading import *
import time

# creating thread instance where count = 3
sem = Semaphore(3)

# creating instance


def display(name):

    # calling acquire method
    print(f'{name}trying to acquire lock')
    sem.acquire()
    print(f'{name}acquired lock')
    for i in range(5):
        time.sleep(1)
        # calling release method
        sem.release()


# creating multiple thread
t1 = Thread(target=display, args=('Thread-1',))
t2 = Thread(target=display, args=('Thread-2',))
t3 = Thread(target=display, args=('Thread-3',))
t4 = Thread(target=display, args=('Thread-4',))
t5 = Thread(target=display, args=('Thread-5',))

# calling the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
