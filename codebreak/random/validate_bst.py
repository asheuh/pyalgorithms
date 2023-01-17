import sys
from binarytree import bst, _build_tree_string

class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right

class Create:
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


class Solution:
    def is_empty(self, stack):
        return len(stack) == 0
    
    def is_valid_bst(self, root: TreeNode) -> bool:
        
        def is_valid(n):
            if not n.right:
                return n.left.val < n.val
            elif not n.left:
                return n.right.val > n.val
            return n.right.val > n.val > n.left.val
        
        stack = []
        explored = []
        stack.append((None, root))
        valid = True
        
        while not self.is_empty(stack) and valid:
            _node = stack.pop()
            r = _node[0]
            node = _node[1]
            
            if node and node not in explored:
                if not node.right and not node.left:
                    explored.append(node)
                    continue
                    
                if is_valid(node):
                    if r:
                        if r.val < node.val:
                            b = node
                            while b.left and b.val > b.left.val:
                                valid = b.left.val > r.val
                                b = b.left
                        elif r.val > node.val:
                            b = node
                            while b.right and b.val < b.right.val:
                                valid = b.right.val < r.val
                                b = b.right
                    stack.append((node, node.left))
                    stack.append((node, node.right))
                else:
                    valid = False
                    break
            explored.append(node)
        return valid


if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()
    print('Enter values separated by comma: ')
    items = list(map(str, input().split(',')))
    print('LENGTH', len(items))
    tree = Create()
    root = None 

    for item in items:
        if item == 'null':
            item = 0
        else:
            item = int(item)
        root = tree.insert_iterative(root, item)
    
    tree.insert_iterative(root, 22)
    tree.insert_iterative(root, 25)
    data = tree.inorder_iter_dfs(root)
    print(tree, data)
    found = tree.search(root, 20)
    print('Found ---> ', found.val)
    print('Successor of found: ', tree.successor(found).val)
    print('Predecessor of found: ', tree.predecessor(found).val)
    lines = _build_tree_string(root, 0, False, '')[0]
    print("\n" + "\n".join((line.rstrip() for line in lines)))

#     s = Solution()
#     result = s.is_valid_bst(root)
#     print(result)
#     key = 20
#     search = tree.search(root, 20)
#     print(search.val == key)
    
