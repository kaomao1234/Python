import threading as th
import time


def func_work(work: int, delay: float):
    for i in range(10):
        print(f"work{work} : {i}")
        time.sleep(delay)


w1 = th.Thread(target=func_work, args=(1, 1.0))
w2 = th.Thread(target=func_work, args=(2, 0.5))
w1.start()
w2.start()
w1.join()
w2.join()
print('----------finish-------'.rjust(20))
