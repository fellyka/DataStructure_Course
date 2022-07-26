# In this simple program , we'll see how threadA and threadB run concurently

import threading
import time
import colorama

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    
    def run(self):
        print(f'Starting thread {self.name}')
        thread_lock.acquire()
        self.thread_count_down(self.name, self.delay)
        thread_lock.release()
        print(f'Finished thread {self.name}')

    def thread_count_down(self,name, delay):
        counter = 5
       

        while counter:
            time.sleep(delay)
            print(f'Thread counting down: {name, counter}')
            counter -= 1

thread_lock = threading.Lock()
       

threadA = MyThread('A',0.5)
threadB = MyThread('B',0.5)

threadA.start()
threadB.start()

threadA.join()
threadB.join()

print('Finished')