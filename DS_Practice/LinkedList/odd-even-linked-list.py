# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenHead = ListNode(-1)
        oddHead = ListNode(-1)
        oddHeadTmp = oddHead
        evenHeadTmp = evenHead
        
        tmp = head
        indices = 0
        while tmp:
            if indices % 2 == 0:
                oddHead.next = ListNode(tmp.val)
                oddHead = oddHead.next
            else:
                evenHead.next = ListNode(tmp.val)
                evenHead = evenHead.next
            tmp = tmp.next
            indices += 1
        oddHead.next = evenHeadTmp.next
        
        return oddHeadTmp.next
        
