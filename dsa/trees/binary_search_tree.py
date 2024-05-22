class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self.find_min(root.right).key
            root.right = self.delete(root.right, root.key)
        return root

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def exists(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self.exists(root.left, key)
        else:
            return self.exists(root.right, key)

# Example usage
bst = BST()
elements = [10, 5, 15, 3, 7, 12, 20]
for elem in elements:
    bst.root = bst.insert(bst.root, elem)

print("Inorder traversal:")
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
inorder(bst.root)

print("\nDeleting 5 and 20:")
bst.root = bst.delete(bst.root, 5)
bst.root = bst.delete(bst.root, 20)
inorder(bst.root)

print("\nDoes 7 exist in the tree?", bst.exists(bst.root, 7))
