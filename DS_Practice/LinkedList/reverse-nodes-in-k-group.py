# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def length(self, h):
        l = 0
        while h:
            l += 1
            h = h.next
        return l

    def reverseKGroup(self, head, k: int):
        l = Solution.length(head)
        tail = new_head = ListNode()

        while head and l >= k:
            tmp_head = head
            prev = None
            for _ in range(k):
                next_ = head.next
                head.next = prev
                prev = head
                head = next_
            tail.next = tmp_head
            tail = head
            l -= k
        if head:
            tail.next = head
        return new_head.next