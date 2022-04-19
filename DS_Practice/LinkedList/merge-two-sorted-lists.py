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
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pq = PriorityQueue()
        
        if not l1 and not l2:
            return None
        
        while l1 or l2:
            if l1:
                pq.put(Helper(l1.val, l1))
            if l2:
                pq.put(Helper(l2.val, l2))
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        tail = head = None
        
        while not pq.empty():
            tmp = pq.get()
            if head is None:
                head = tmp.node
                tail = head
            
            tail.next = tmp.node
            tail = tail.next
        tail.next = None
        
        return head
