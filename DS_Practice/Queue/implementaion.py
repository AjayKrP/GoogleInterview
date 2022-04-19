class Queue:
    def __init__(self, size):
        self.__size = size
        self.__queue = [-1] * self.__size
        self.__rear = -1
        self.__front = -1

    def enqueue(self, item):
        if self.__front + 1 == self.__size:
            raise OverflowError('Queue Overflow')
        if self.__rear == -1 and self.__front == -1:
            self.__rear = self.__front = 0
        else:
            self.__front += 1
        self.__queue[self.__front] = item

    def dequeue(self):
        if self.__rear == -1 or self.__rear > self.__front:
            raise MemoryError('Queue Underflow')
        item = self.__queue[self.__rear]
        if self.__rear == self.__front:
            self.__rear = self.__front = -1
        else:
            self.__rear += 1
        return item

    def peek(self):
        if self.__rear >= 0:
            return self.__queue[self.__rear]
        return None

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(9)
print(queue.peek())
