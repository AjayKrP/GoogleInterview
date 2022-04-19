# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if k <= 0:
            return head
        if head.next is None:
            return head

        prev = self.rotateRight(head.next, k-1)
        head.next = head.next.next

        return prev


