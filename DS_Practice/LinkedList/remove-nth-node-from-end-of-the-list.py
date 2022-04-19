# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        fast = head
        
        while n > 0:
            fast = fast.next
            n -= 1
            
        if fast is None:
            return head.next
        
        slow = head
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return head
        
