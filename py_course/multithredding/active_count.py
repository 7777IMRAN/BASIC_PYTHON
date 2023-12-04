import time
from threading import *
print('the number of threads executing',active_count())
def add(a,b):
    time.sleep(2)
    print(a+b)
t1=Thread(target=add,args=(10,),kwargs=({'b':20}))
t2=Thread(target=add,args=(20,),kwargs=({'b':30}))
t3=Thread(target=add,args=(30,),kwargs=({'b':40}))
t1.start()
t2.start()
t3.start()
print('the number of threads executing',active_count())