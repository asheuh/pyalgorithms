from queue import Queue


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def height(root: TreeNode):
    q = Queue()
    q.put(root)
    q.put(None) # we need this to know the end of the height
    h = 0 # Height of binary tree

    while not q.empty():
        node = q.get()
        if not node:
            h += 1

        if node:
            # Add left ond right if they exist
            if node.left:
                q.put(node.left)
            
            if node.right:
                q.put(node.right)
        elif not q.empty():
            q.put(None)
    return h
