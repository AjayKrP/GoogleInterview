# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseEvenLengthGroups(self, head):
        tmp = head
        l = 0
        while tmp:
            l += 1
            tmp = tmp.next
        k = [x for x in range(1, l+1)]
        new_head = tail = ListNode()
        idx = 0
        cnt = 0
        while head and l >= idx + k[idx]:
            if k[idx] % 2 == 0:
                tmp_head = head
                prev = None

                for _ in range(idx, idx + k[idx]):
                    nxt = head.next
                    head.next = prev

                    prev = head
                    head = nxt
                tail.next = prev
                tail = tmp_head
            else:
                head = head.next

            idx = k[cnt]
            cnt += 1

        if head:
            tail.next = head
        return new_head.next

