from threading import Thread
from time import sleep
class A(Thread):
    def run(self):
        for i in range(5):
            print("Swarup")
            sleep(1)
        
class B(Thread):
    def run(self):
        for i in range(5):
            print("Dash")
            sleep(1)
        
a=A()
b=B()

a.start()
b.start()

a.join() #join -- Whenever this method is called for any Thread object, it blocks the calling thread till the time the thread whose join() method is called terminates.
b.join()

print("Its a BRAND")