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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()
        
       
        for l1 in lists:
            while l1:
                if l1:
                    pq.put(Helper(l1.val, l1))
                
                l1 = l1.next if l1 else None

        tail = head = None

        while not pq.empty():
            tmp = pq.get()
            if head is None:
                head = tmp.node
                tail = head

            tail.next = tmp.node
            tail = tail.next
            
        if not tail:
            return None
        tail.next = None 
        
        return head

