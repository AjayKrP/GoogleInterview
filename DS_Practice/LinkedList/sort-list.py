# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Helper(object):
    def __init__(self, val, node):
        self.val = val
        self.node = node
       
    def __cmp__(self, other):
        return cmp(self.val, other.val)
    
    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val
    
class Solution:
    

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pq = PriorityQueue()
        if not head:
            return head
        tmp = head
        while tmp:
            pq.put(Helper(tmp.val, tmp))
            tmp = tmp.next
        
        tail = None
        head = None
        while not pq.empty():
            tmp = pq.get().node
            
            #print(tmp[0], tmp[1].val)
            if not head:
                head = tmp
                tail = tmp
            else:
                tail.next = tmp
                tail = tmp
        tail.next = None
        
        return head


class Solution1:

    def sortList(self, head):
        tmp1 = head
        tmp2 = head
        while tmp1 and tmp1.next:
            tmp2 = tmp1.next
            while tmp2:
                if tmp1.val > tmp2.val:
                    tmp2.val, tmp1.val = tmp1.val, tmp2.val
        return head

