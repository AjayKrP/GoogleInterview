"""
Since processes dont share data with another processes. So we have to use Value -> for Single Value Copy
Array -> For multiple Values copy
"""

from multiprocessing import Process, Value, Array, Lock, Pool
from multiprocessing import Queue
import os
import time

num_processes = os.cpu_count()


def add_one_100(num, lock):
    for i in range(100):
        with lock:  # use lock as a context manager to avoid writing acquire & release methods
            num.value += 1
        time.sleep(0.01)  # race condition : processes try to modify variable at same time


def add_one_100_array(numbers, lock):
    for i in range(100):
        with lock:  # use lock as a context manager to avoid writing acquire & release methods
            for i in range(len(numbers)):
                numbers[i] += 1
        time.sleep(0.01)  # race condition : processes try to modify variable at same time


def example_share_single_value():
    lock = Lock()
    shared_number = Value('i', 0)  # i(first arguments) denotes data type -> here it is integer
    print('starting value: ', shared_number.value)

    p1 = Process(target=add_one_100, args=(shared_number, lock,))
    p2 = Process(target=add_one_100, args=(shared_number, lock,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('end number: ', shared_number.value)


def example_share_array_values():
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array at the begining: ', shared_array[:])

    p1 = Process(target=add_one_100_array, args=(shared_array, lock,))
    p2 = Process(target=add_one_100_array, args=(shared_array, lock,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('array at the end: ', shared_array[:])


def square(numbers, q, lock):
    for i in numbers:
        q.put(i * i)


def make_negative(numbers, q, lock):
    for i in numbers:
        q.put(-1 * i)


def example_queue_with_multiprocessing():
    lock = Lock()
    q = Queue()
    numbers = range(1, 6)
    p1 = Process(target=square, args=(numbers, q, lock,))
    p2 = Process(target=make_negative, args=(numbers, q, lock,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())


def cube(number):
    return number * number * number


def example_process_pool():
    numbers = range(10)
    pool = Pool()
    # methods available: map, apply, join, close
    result = pool.map(cube, numbers) # allocate maximum number of process for do the computations
    pool.close()
    pool.join()
    print(result)


if __name__ == "__main__":
    example_share_single_value()
    example_share_array_values()
    example_queue_with_multiprocessing()
    example_process_pool()
