from threading import Thread, Lock, current_thread
import time

"""
How to share data between threads? 
"""

database_value = 0


def increase(lock):
    global database_value

    # we can use context manager to avoid writing lock.acquire and lock.release functions
    with lock:
        local_copy = database_value
        local_copy += 1
        # race condition occurs because of computation time, so we have to use locking mechanism
        time.sleep(0.1)
        database_value = local_copy


def example_1():
    print('start value', database_value)

    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)


from queue import Queue


def worker(q, lock):
    while True:
        front = q.get()  # thread safe
        # we had to add context manager here because more than 1 threads were trying to print at same time
        with lock:
            print(f'current thread: {current_thread().name}, val: {front}')
        time.sleep(0.1)  # one thread is waiting then another thread will start
        q.task_done()


def example_2():
    q = Queue()
    num_threads = 10
    lock = Lock()
    for _ in range(num_threads):
        thread = Thread(target=worker, args=(q, lock,))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)  # thread safe

    q.join()


if __name__ == "__main__":
    example_1()
    example_2()
