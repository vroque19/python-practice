# create a tree data structure
# implement search, insert, and remove
#
class TreeNode(object):
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1

    def search(root, key):
        # Base cases: root is null, or is the key
        if root is None or root.val == key:
            return root
        elif root.val < key:
            return search(root.right, key)
        else:
            return search(root.left, key)

    def insert(root, key):
        if root is None:
            return TreeNode(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = insert(root.right, key)
            else:
                root.left = insert(root.left, key)
    return root
        


# create an AVL tree
