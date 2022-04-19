class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            tmp = Node(data)
            tmp.next = self.head
            self.head.prev = tmp
            self.head = tmp

    def print(self):
        tmp = self.tail
        while tmp:
            print(tmp.data)
            tmp = tmp.prev


dll = DLL()
dll.push(4)
dll.push(5)
dll.push(6)
dll.push(8)
dll.push(9)
dll.push(1)
dll.print()

