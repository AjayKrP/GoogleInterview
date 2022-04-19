# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findTarget(self, root, k: int) -> bool:
#         diffArr = {}
#
#         def search(root, val):
#             if root:
#                 if val == root.val:
#                     return True
#                 elif val < root.val:
#                     return search(root.left, val)
#                 elif val > root.val:
#                     return search(root.right, val)
#                 else:
#                     return False
#
#         def helper(root):
#             if root:
#                 helper(root.left)
#                 diff = k - root.val
#                 if search(root, diff):
#                     return True
#                 helper(root.right)
#
#             return False
#
#         return helper(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue


class Solution:
    def findTarget(self, root, k: int) -> bool:
        seen = set()
        q = Queue()
        q.put(root)
        while not q.empty():
            front = q.get()
            diff = k - front.val
            if diff in seen:
                return True
            seen.add(diff)
            if root.left:
                q.put(front.left)
            if root.right:
                q.put(front.right)
        return False
