class Node:
    def __init__(self, fred, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None


def huffman_decoding(root: Node, s: str):
    # Problem: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?isFullScreen=true
    results = []
    node = root
    for i, bit in enumerate(s):
        if bit == '0':
            node = node.left
            if not node.data == '\x00':
                results.append(node.data)
        else:
            node = node.right
            if not node.data == '\x00':
                results.append(node.data)

        if not node.right and not node.left:
            node = root
    return ''.join(results)
