class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''

        queue = deque()
        queue.append(root)
        res = [str(root.val)]

        while queue:
            node = queue.popleft()
            for child in node.left, node.right:
                res.append(str(child.val) if child else 'n')
                if child:
                    queue.append(child)

        return ' '.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        data = deque([i if i != 'n' else None for i in data.split()])
        root = TreeNode(data.popleft())
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            left, right = data.popleft(), data.popleft()

            if left:
                node.left = TreeNode(left)
                queue.append(node.left)

            if right:
                node.right = TreeNode(right)
                queue.append(node.right)

        return root