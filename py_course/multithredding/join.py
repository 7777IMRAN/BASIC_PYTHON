import time
from threading import *
def download():
    print('document is downloading')
    # time.sleep(5)
    print('document is downloaded')

def notification():
    print('open with')

t1=Thread(target=download)
t2=Thread(target=notification)
t1.start()
# t1.join()   #t2 will wait until t1 thread is executes
t2.start()
# t2.join()
