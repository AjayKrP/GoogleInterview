# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        res = [0]
        def helper(root):
            if root is None:
                return
            helper(root.right)
            res.append(res[-1] + root.val)
            root.val = res[-1]
            helper(root.left) 
        helper(root)
            
        
        return root
