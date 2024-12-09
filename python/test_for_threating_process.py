import os
import time
import threading
import multiprocessing


class Main_task:
    def long_time_task(self):
        pass
    
    
class test_normal_run(Main_task):
    
    def long_time_task(self):
        print(f'The current process {os.getpid()}')
        time.sleep(2)
        print(f'result: {8**20}')
        
    def run(self):
        print(f'The parent process is {os.getpid()}')
        for i in range(2):
            self.long_time_task()
            
        
class test_multi_process(Main_task):
    
    def long_time_task(self, i):
        print(f'Sub-process:{os.getpid()} - task {i}')
        time.sleep(2)
        print(f'Result: {8**20}')
        
    def run(self):
        print(f'Current parent process {os.getpid()}')
        p1 = multiprocessing.Process(target = self.long_time_task, args = (1,))
        p2 = multiprocessing.Process(target = self.long_time_task, args = (2,))
        print(f'Waiting for sub-process completed')
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        

class test_multi_threading(Main_task):
    
    def long_time_task(self,j):
        print(f'Current sub-thread: {threading.current_thread()}, task - {j}')
        time.sleep(2)
        print(f'Result: {8**20}')
        
    def run(self):
        print(f'The main thread : {threading.current_thread().name}')
        thread_list = []
        for k in range(1,3):
            t = threading.Thread(target = self.long_time_task, args = (k,))
            thread_list.append(t)
            
        for t in thread_list:
            t.start()
            
        for t in thread_list:
            t.join()

if __name__ == '__main__':
    start = time.time()
    
    # # Test for normal run
    # test1 = test_normal_run()
    # test1.run()
    
    # # Test for multi-process
    # test2 = test_multi_process()
    # test2.run()
    
    # Test for multi-thread
    test3 = test_multi_threading()
    test3.run()
    
    end = time.time()
    print(f'Total using time is {end - start}')