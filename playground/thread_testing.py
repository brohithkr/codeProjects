from threading import Thread
import math
import time

def print_range(a,b):
    for i in range(a,b):
        if i == int((a+b)//2):
            print("Waiting...")
            time.sleep(3)
        print(i)

t1 = Thread(target=print_range, args=(0,9))
t2 = Thread(target=print_range, args=(10,20))

t1.start()
t2.start()
# t1.join()
# t2.join()