class Solution:
    def __init__(self):
        self.deepest = float('-inf')
        self.deepestNode = None

    def subtreeWithAllDeepest(self, root):

        def helper(root, prnt, lvl):
            if root is None:
                return
            if lvl > self.deepest:
                self.deepest = lvl
                self.deepestNode = prnt

            helper(root.left, root, lvl + 1)
            helper(root.right, root, lvl + 1)

        helper(root, None, 0)
        if self.deepestNode:
            if self.deepestNode.left and self.deepestNode.right:
                return self.deepestNode
            elif self.deepestNode.left:
                return self.deepestNode.left
            elif self.deepestNode.right:
                return self.deepestNode.right
        else:
            return root