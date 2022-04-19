# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = Queue()
        q.put(root)
        dl = self.height(root)
        out = 0
        while not q.empty():
            qL = q.qsize()
            while qL:
                item = q.get()
                if dl == 1:
                    out += item.val
                    
                if item.left:
                    q.put(item.left)
                if item.right:
                    q.put(item.right)
                qL -= 1
            dl -= 1
            
        return out
    def height(self, root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return max(lh, rh) + 1
### ONLY USING DFS
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dl = self.height(root)
        return self.findDeepedestLeaveSum(root, dl, 1)
        
    def findDeepedestLeaveSum(self, root, dl, level):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            if level > dl:
                out = root.val
                dl = level
                
            elif dl  == level: 
                return root.val
        return self.findDeepedestLeaveSum(root.left, dl, level + 1) + self.findDeepedestLeaveSum(root.right, dl, level + 1)
        
        
    def height(self, root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return max(lh, rh) + 1
"""
