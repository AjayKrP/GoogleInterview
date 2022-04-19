# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        tree = defaultdict(list)
        level = 0
        for c in traversal:
            if c.isdigit():
                tree[level].append(c)
                level = 0
            else:
                level += 1
        root = None
        for item in tree.items():            
            for i in range(len(item[1])):
                root = self.createTree(root, item[1][i])
                print(item[1][i])
        return root
                
    def createTree(self, root, value):
        if root is None:
            return TreeNode(value)
        if root.left is None:
            root.left = self.createTree(root.left, value)
        elif root.right is None:
            root.right = self.createTree(root.right, value)
        
        return root
                
       # TODO 
