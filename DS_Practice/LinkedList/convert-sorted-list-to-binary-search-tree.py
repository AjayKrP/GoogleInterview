# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        pre = head
        fast = slow = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root


class Solution1:
    def sortedListToBST(self, head):
        def buildlist(head):
            stack=[]
            if not head:
                return []
            temp=head
            while temp:
                stack.append(temp.val)
                temp=temp.next
            return stack
        def conversion(stack):
            if len(stack)==0:
                return
            mid=len(stack)//2
            temp=TreeNode(stack[mid])
            temp.left=conversion(stack[:mid])
            temp.right=conversion(stack[mid+1:])
            return temp
        stack=buildlist(head)
        return conversion(stack)
