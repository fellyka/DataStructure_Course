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
        self.thread_count_down(self.name, self.delay)
        print(f'Finished thread {self.name}')

    def thread_count_down(self,name, delay):
        counter = 5

        while counter:
            time.sleep(delay)
            print(f'Thread counting down: {name, counter}')
            counter -= 1


print()

threadA = MyThread('A',0.5)
threadB = MyThread('B',0.5)

if(threadA.is_alive()):
    print('ThreadA/B are alive ')
else:
    print('ThreadA/B are not YET alive ')

print()

threadA.start()
threadB.start()

if(threadA.is_alive()):
    print('ThreadA/B SHOULD BE alive NOW')
else:
    print('ThreadA/B are not alive ')

print()

threadA.join()
threadB.join()

print()

if(threadA.is_alive()):
    print('ThreadA is alive ')
else:
    print('ThreadA/B are no longer alive')

print()

print('Finished')