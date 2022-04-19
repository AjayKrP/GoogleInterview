# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def genTree(mn, mx):
            if mn > mx:
                return [None]

            ans = []
            for i in range(mn, mx + 1):
                left_tree = genTree(mn, i - 1)
                right_tree = genTree(i + 1, mx)
                for lchild in left_tree:
                    for rchild in right_tree:
                        root = TreeNode(i)
                        root.left = lchild
                        root.right = rchild
                        ans.append(root)
            return ans

        if n == 0: return []
        return genTree(1, n)
