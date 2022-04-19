# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []

    def dfs(self, root):
        if root:
            if root.left:
                self.stack.append(root)
                self.dfs(root.left)
                self.dfs(root.right)

    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        for i in range(0, len(self.stack)-1):
            node = self.stack[i]
            node.left = node.right = None
            node.right = self.stack[i+1]




