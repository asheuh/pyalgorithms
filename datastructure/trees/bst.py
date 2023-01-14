"""
Binary Search Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    # Insert, deletion, search takes on average O(log n) time. n being the number of nodes
    def __init__(self):
        self.sorted_list = []
        self.size = 0

    def search(self, root, key):
        while root:
            if key == root.val:
                return root

            if root.val > key:
                root = root.left
            elif root.val < key:
                root = root.right
        return root

    def __repr__(self):
        return f'TreeNode: ({self.sorted_list} -> {self.size})'

    def minimum(self, node):
        while node.left:
            node = node.left
        return node

    def maximum(self, node):
        while node.right:
            node = node.right
        return node

    def successor(self, x):
        if x.right:
            return self.minimum(x.right)
        
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left:
            return self.maximum(x.left)

        y = x.parent
        while y and x == y.left:
            x = y
            y = y.parent
        return y

    def insert_iterative(self, root, v):
        self.size += 1
        new_node = TreeNode(val=v)
        y = None
        x = root
        while x:
            y = x
            if v < x.val:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if not y:
            root = new_node
        elif new_node.val < y.val:
            y.left = new_node
        else:
            y.right = new_node
        return root

    def insert_recursion(self, root, value):
        if not root:
            self.size += 1
            return TreeNode(val=value)

        if root.val == value:
            return root

        if root.val > value:
            root.left = self.insert_recursion(root.left, value) 
        elif root.val < value:
            root.right = self.insert_recursion(root.right, value)
        return root

    def inorder(self, root):
        if not root:
            return root
        self.inorder(root.left)
        self.sorted_list.append(root.val)
        self.inorder(root.right)

    def preorder(self, root):
        if not root:
            return root
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return root
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)

    def preorder_iter_dfs(self, root):
        if not root:
            return
        items = []
        stack = [root]
        while stack:
            node = stack.pop()
            items.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return items

    def inorder_iter_dfs(self, root):
        if not root:
            return

        items = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                items.append(node.val)
                root = node.right
        return items

    def post_order_iterative_dfs(self, root):
        if not root:
            return
        items = []
        last = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last != peek_node.right:
                    root = peek_node.right
                else:
                    items.append(peek_node.val)
                    last = stack.pop()

