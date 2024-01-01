class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def addNode(self, root, val):
        if root is None:
            self.root = TreeNode(val)
            return root
        if root.left is None:
            root.left = self.addNode(root.left, val)
        elif root.right is None:
            root.right = self.addNode(root.right, val)
        
