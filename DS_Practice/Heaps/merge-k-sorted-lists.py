# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Helper:
    def __init__(self, val, node):
        self.val = val
        self.node = node

    def __lt__(self, other):
        return self.val < other.val
    

class Solution:
    def mergeKLists(self, lists):
        pq = PriorityQueue()

        for l in lists:
            while l:
                if l:
                    pq.put((l.val, l))
                l = l.next if l else None

        dummyHead = ListNode(float('-inf'))
        tail = dummyHead
        head = tail
        while not pq.empty():
            front = pq.get()

            tail.next = front[1]
            tail = tail.next

        return dummyHead.next
