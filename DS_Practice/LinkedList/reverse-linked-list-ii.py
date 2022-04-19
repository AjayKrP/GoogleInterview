# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left: int, right: int):
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        tmp = head
        for _ in range(left - 1):
            tmp = tmp.next
        curr = tmp
        curr_head = curr
        prev = None
        for _ in range(left, right):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr_head.next = curr
        tmp.next = prev

        return head



