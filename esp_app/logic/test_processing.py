import multiprocessing
import time

def worker_process(process_id):
    while True:
        print(f"Process {process_id} is running.")
        time.sleep(1)  # Simulate some work

if __name__ == "__main__":
    num_processes = 4  # You can adjust the number of processes as needed
    processes = []

    for i in range(num_processes):
        process = multiprocessing.Process(target=worker_process, args=(i,))
        processes.append(process)
        process.start()

    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print("Terminating processes...")
        for process in processes:
            process.terminate()

    print("All processes have been terminated.")
