# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        tmp = l1
        while tmp:
            stack1.append(tmp.val)
            tmp = tmp.next
        
        tmp = l2
        while tmp:
            stack2.append(tmp.val)
            tmp = tmp.next
        
        result = []
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0:
            l1v = stack1.pop() if len(stack1) > 0 else 0
            l2v = stack2.pop()  if len(stack2) > 0 else 0
            
            carry, out = divmod(l1v + l2v + carry, 10)
            
            result.append(out)
        
        if carry > 0:
            result.append(carry)
        
        dummyHead = ListNode(-1)
        head = dummyHead
        while len(result) > 0:
            val = result.pop()
            head.next = ListNode(val)
            head = head.next
        
        return dummyHead.next
            
        
