# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        tmp = head
        while tmp:
            l += 1
            tmp = tmp.next
        
        window_size = l//k
        tmp = head
        result = []
        dummyHead = ListNode(-1)
        tmpHead = dummyHead
        cnt = 0

        while tmp:
            
            if (cnt < window_size):
                tmpHead.next = ListNode(tmp.val)
                tmpHead = tmpHead.next
            else:
                cnt = 0
                result.append(dummyHead.next)
                dummyHead = ListNode(-1)
                tmpHead = dummyHead
            cnt += 1
            tmp = tmp.next
        return result
        
                
            
        
