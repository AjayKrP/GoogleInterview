# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        arr = []
        n = 0
        tmp = head
        while  tmp:
            arr.append(tmp.val)
            tmp = tmp.next
            n += 1
        
        arr[k-1], arr[n-k] = arr[n-k], arr[k-1]
        
        dummyHead = ListNode(-1)
        head = dummyHead
        for i in range(n):
            head.next = ListNode(arr[i])
            head = head.next
        
        return dummyHead.next
        
