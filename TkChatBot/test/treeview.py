import threading
import queue as Queue

cmdqueue = Queue.Queue()
def workerThread(queobject):
    #  for i in range(10): 
    while True:
            vars = queobject.get()
        #   print(f'Round {i} : {vars}')
            print(vars)
            queobject.task_done()
            print('loop is working.')
for i in range(10):
    worker = threading.Thread(target=workerThread, args=(cmdqueue,))
    # worker.setDaemon(True)
    cmdqueue.put(f'work{i} - {i}')
    worker.start()