# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 0
            # if root.left is None and root.right is None:
            #     return 1
            # if root.left and root.right and root.left.val==root.right.val==root.val:
            #     return 2
            l = helper(root.left)
            r = helper(root.right)
            la = ra = 0
            if root.left and root.left.val == root.val:
                la = l + 1
            if root.right and root.right.val == root.val:
                ra =  r + 1
            self.ans = max(self.ans, la + ra)
            return max(la, ra)
        self.ans = 0
        helper(root)
        return self.ans
        
        if root is None:
            return 0
        print(helper(root))
        self.longestUnivaluePath(root.left)
        self.longestUnivaluePath(root.right)
            
        
