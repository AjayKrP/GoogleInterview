# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = TreeNode(float('-inf'))
        self.res = []
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root is not None:
                helper(root.left)

                if (root.val < self.prev.val):
                    self.res.append([root, self.prev])


                self.prev = root
                helper(root.right)
                
        helper(root)
        s1 = self.res[0]
        s2 = self.res[-1]
        
        s1[1].val, s2[0].val = s2[0].val, s1[1].val
        
