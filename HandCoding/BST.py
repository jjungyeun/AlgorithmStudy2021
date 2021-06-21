class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def _insert_data(root, data):
            if root.data >= data:
                if root.left:
                    _insert_data(root.left, data)
                else:
                    root.left = TreeNode(data)
            else:
                if root.right:
                    _insert_data(root.right, data)
                else:
                    root.right = TreeNode(data)

        if self.root:
            _insert_data(self.root, data)
        else:
            self.root = TreeNode(data)

    def find(self, key):
        def _find_key(root, key):
            if root is None:
                return False
            if root.data == key:
                return True
            elif root.data > key:
                return _find_key(root.left, key)
            else:
                return _find_key(root.right, key)
        return _find_key(self.root, key)

    def delete(self, key):
        def _delete_key(root, key):
            if root is None:
                return root, False

            deleted = False
            if root.data == key:
                deleted = True

                if root.left and root.right:
                    parent, child = root, root.right
                    while child.left:
                        parent, child = child, child.left
                    child.left = root.left
                    if parent != root:
                        parent.left = child.right
                        child.right = root.right
                    root = child
                elif root.left or root.right:
                    root = root.left or root.right
                else:
                    root = None
            elif root.data > key:
                root.left, deleted = _delete_key(root.left, key)
            else:
                root.right, deleted = _delete_key(root.right, key)

            return root, deleted

        self.root, deleted = _delete_key(self.root, key)
        return deleted

    def printTree(self):
        def _dfs(here, depth):
            print(here.data, depth)
            if here.left:
                _dfs(here.left, depth+1)
            if here.right:
                _dfs(here.right, depth+1)

        _dfs(self.root, 1)


bst = BinarySearchTree()
bst.insert(5)
bst.insert(2)
bst.insert(7)
bst.insert(9)
bst.insert(6)
bst.insert(3)
bst.printTree()

print(bst.find(4))
print(bst.find(6))

bst.delete(5)
bst.printTree()