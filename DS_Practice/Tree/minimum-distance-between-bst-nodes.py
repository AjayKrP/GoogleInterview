class Solution:
    def __init__(self):
        self.x = -1
        self.mn = float('inf')

    def minDiffInBST(self, root):
        if root is None:
            return 0
        self.minDiffInBST(root.left) 
        if self.x == -1:
            self.x = root.val
        else:
            self.mn = min(self.mn, abs(self.x - root.val))
            self.x = root.val
        self.minDiffInBST(root.right) 

        return self.mn