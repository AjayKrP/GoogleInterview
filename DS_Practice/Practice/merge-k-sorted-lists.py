# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        q = PriorityQueue()

        dummyHead = ListNode(-1)
        head = dummyHead

        for ll in A:
            while ll:
                q.put((ll.val, ll))
                ll = ll.next
        
        while not q.empty():
            front = q.get()
            tmp = ListNode(front[0])
            head.next = tmp
            head = tmp
        
        return dummyHead.next

