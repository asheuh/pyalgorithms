"""
Imports
"""
from typing import List
from recursioncounter import RecursionCounter


class Node:
    """
    main node
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self) -> int:
        return 1 + max(self.left.height() if self.left else 0,
                       self.right.height() if self.right else 0)

    def is_leaf(self) -> bool:
        if self.height() > 0:
            return True
        return False

    def update_height(self):
        pass


class BinarySearchTree:
    """
    Binary search tree
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self) -> bool:
        """
        >>> node = BinarySearchTree()
        >>> node.is_empty()
        True
        >>> node.add(12)
        >>> node.is_empty()
        False
        """
        if not self.root:
            return True
        return False

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return 'BinarySearchTree <class>'

    def height(self) -> int:
        """
        height of the tree (height of the root node)
        """
        if not self.root:
            return 0
        return self.root.height()

    def add_helper(self, node, key):
        """
        a helper method to recursively add items to the tree
        """
        if not node:
            return Node(key)  # Address of a new node
        if key < node.key:
            node.left = self.add_helper(node.left, key)
        elif key > node.key:
            node.right = self.add_helper(node.right, key)
        return node

    def add(self, key):
        """
        insert a new item to the tree
        >>> node = BinarySearchTree()
        >>> node.add(1)
        >>> node.add(2)
        >>> node.add(3)
        >>> node.add(4)
        >>> node.add(5)
        >>> node.add(6)
        >>> node.is_empty()
        False
        >>> node.root.key
        6
        """
        _ = RecursionCounter()
        self.root = self.add_helper(self.root, key)
        self.size += 1

    def preorder(self, node: Node):
        """
	>>> root = Node(1)
        >>> node2 = Node(2)
        >>> node3 = Node(3)
        >>> node4 = Node(4)
        >>> node5 = Node(5)
        >>> node6 = Node(6)
        >>> node7 = Node(7)
        >>> root.left, root.right = node2, node3
        >>> node2.left, node2.right = node4 , node5
        >>> node3.left, node3.right = node6 , node7
        >>> pre_order(root)
        1 2 4 5 3 6 7
        """
        _ = RecursionCounter()
        stack: List[Node] = []
        if node:
            print(node.key, end=",")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node: Node):
        _ = RecursionCounter()

        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    def remove_helper(self, node: Node, key) -> None:
        """
        a helper method to recursively add items to the tree
        """
        if not node:
            return node
        if key < node.key:
            node.left = self.remove_helper(node.left, key)
        elif key > node.key:
            node.right = self.remove_helper(node.right, key)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp
            successor = self.find_min(node.right)
            node.key = successor.key
            node.right = self.remove_helper(node.right, successor.key)
        self.size -= 1
        return node

    def remove(self, key):
        """
        removes a node
        >>> node = BinarySearchTree()
        >>> node.add(12)
        >>> node.add(13)
        >>> node.remove(12)
        >>> node.find(12)
        None
        """
        _ = RecursionCounter()
        return self.remove_helper(self.root, key)

    def find_min(self, node: Node) -> Node:
        """
        finds the minimum node of a subtree
        """
        current_node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def find_helper(self, node: Node, key):
        """
        Find helper finction
        """
        if not node or key == node.key:
            return node
        if key < node.key:
            if node.left:
                return self.find_helper(node.left, key)
        if key > node.key:
            if node.right:
                return self.find_helper(node.right, key)

    def find(self, key):
        """
        >>> node = BinarySearchTree()
        >>> node.add(12)
        >>> node.add(13)
        >>> node.find(12)
        12
        """
        _ = RecursionCounter()
        return self.find_helper(self.root, key)
