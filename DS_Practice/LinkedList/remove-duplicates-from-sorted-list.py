# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        left = right = head

        while right and right.next:
            while right and right.next and left.val == right.next.val:
                right = right.next

            left.next = right
            left = right.next
        return head
