class BinarySearchTree:
    def __init__(self, root):
        self._root = root


    def insert(self, node):
        current = self._root

        while current is not None:
            if node < current:
                if current.left is None:
                    current.left = node
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                else:
                    current = current.right
