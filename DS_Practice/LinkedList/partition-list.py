# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        leftList = ListNode()
        rightList = ListNode()
        leftHead = leftList
        rightHead = rightList

        tmp = head
        while tmp:
            if tmp.val < x:
                leftList.next = ListNode(tmp.val)
                leftList = leftList.next
            else:
                rightList.next = ListNode(tmp.val)
                rightList = rightList.next

        leftList.next = rightHead.next

        return leftList.next
