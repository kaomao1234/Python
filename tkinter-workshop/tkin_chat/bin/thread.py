import threading
import time

# Lock to serialize console output
output = threading.Lock()

def threadfunc(a,b):
    for i in range(a,b):
        time.sleep(.01) # sleep to make the "work" take longer
        with output:
            print(i)

# Collect the threads
threads = []
for i in range(10,100,10):
    # Create 9 threads counting 10-19, 20-29, ... 90-99.
    thread = threading.Thread(target=threadfunc,args=(i,i+10))
    threads.append(thread)

# Start them all
for thread in threads:
    thread.start()

# Wait for all to complete
for thread in threads:
    thread.join()

print("finist all thread")