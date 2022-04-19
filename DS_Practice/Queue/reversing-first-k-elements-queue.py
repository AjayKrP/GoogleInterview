from queue import Queue

def reverseFirstKElements(k, q):
    if q.empty() == True or k > q.qsize() or k <= 0:
        return

    Stack = []
    # put the first K elements into a Stack
    for i in range(k):
        Stack.append(q.queue[0])
        q.get()

    # Enqueue the contents of stack at the back of the queue
    while (len(Stack) != 0):
        q.put(Stack[-1])
        Stack.pop()

    # Remove the remaining elements and enqueue them at the end of the q
    for i in range(q.qsize() - k):
        q.put(q.queue[0])
        q.get()

    return q.queue


# Driver code
if __name__ == '__main__':
    q = Queue()
    q.put(10)
    q.put(20)
    q.put(30)
    q.put(40)
    q.put(50)
    q.put(60)
    q.put(70)
    q.put(80)
    q.put(90)
    q.put(100)

    k = 5
    print(reverseqFirstKElements(k, q))
