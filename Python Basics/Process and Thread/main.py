"""
Process: is an instance of program (eg. Python interpreter, starting chrome browser)

+ process takes advantages of multiple CPUs and Cores
+ It has separate memory space -> Memory is not shared between processes
+ Great for CPU bound processing
+ New Processes start independently from other processes
+ Processes are interruptable/killable
+ One GIL(Global Interpreter Lock) for each process -> Avoid GIL limitations.

- Heavyweight
- Process starting time is more than thread
- More memory
- IPC(inter-process communication) is more complicated


Thread: is an entity within process that can be scheduled(also know as "lightweight process")
A process can spawn multiple threads

+ All threads within process share the same memory
+ Lightweight
+ Starting a thread is faster than starting a process
+ Great for IO bound tasks

- Threading is limited by GIL -> Only one thread at a time
- No effects for CPU bound tasks
- Not intractable/Killable
- Careful with race condition(Memory leaks)


GIL(Global Interpreter Lock)
A program that allow only one thread at a time to execute in Python

- Needed in Cpython because memory management is not thread safe

- Avoid
    - Use Multiprocessing
    - Use a different free-threaded python implementation (Jython, IronPython)
    - Use Python as a wrapper for third party library (C/C++) - numpy,scipy
"""
## Multiprocessing
from multiprocessing import Process
import os
import time

processes = []
num_process = os.cpu_count()


def square(x):
    for i in range(x):
        i * i
        time.sleep(0.1)


for _ in range(num_process):
    p = Process(target=square, args=(100,))
    processes.append(p)

# Start all the process
for process in processes:
    process.start()

# wait till all process finish
for process in processes:
    process.join()

print('end main process')

## Threading

from threading import Thread

num_threads = 10
threads = []
for _ in range(num_threads):
    thread = Thread(target=square, args=(100,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
