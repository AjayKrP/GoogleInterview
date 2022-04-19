# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.prev = 0
        self.res = 0
        def helper(root, t):
            if root is None:
                return 0
            
            t = (t * 10) + root.val

            if root.left is None and root.right is None:
                return t
            #if root.left is None and root.right is None:

            return helper(root.left, t) + helper(root.right, t)

        return helper(root, 0)
        
        return self.res
