class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class SingleLL:
    def __init__(self) -> None:
        self.head = None
    
    def insert_at_head(self, val):
        if (self.head is None):
            self.head = Node(val)
        else:
            tmpNode = Node(val)
            tmpNode.next = self.head
            self.head = tmpNode

    def insert_at_tail(self, val):
        if (self.head is None):
            self.head = Node(val)
        else:
            tmpNode = Node(val)
            self.head.next = tmpNode
            self.head = tmpNode

    def insert_after_specific_node(self, node, val):
        if (self.head is None):
            self.head = Node(val)
        else:
            currentHead = self.head
            while currentHead and currentHead.next and currentHead.next.val != node:
                currentHead = currentHead.next
            tmpNode = Node(val)
            if currentHead:
                nextNode = currentHead.next
                currentHead.next = tmpNode
                tmpNode.next = nextNode
            else:
                self.head.next = tmpNode
                self.head = tmpNode


    def remove_node(self, val):
        pass

    def remove_from_tail(self):
        pass

    def remove_from_head(self):
        pass

    def __str__(self) -> str:
        tmpHead = self.head
        while tmpHead:
            print(tmpHead.val)
            tmpHead = tmpHead.next

    def has_cycle(self):
        pass



ll = SingleLL()
ll.insert_at_head(2)
ll.insert_at_head(3)
ll.insert_at_head(4)
ll.insert_at_head(5)
ll.insert_at_head(6)
print(ll)
