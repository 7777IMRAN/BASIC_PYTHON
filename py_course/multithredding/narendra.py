from threading import *
import time
def ns(a,b):
    print(a+b)

t1=Thread(target=ns,args=(10,20))
t1.start()

