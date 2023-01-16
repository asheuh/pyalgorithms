"""
Import
"""
import sys
from binarytree import bst, _build_tree_string

from pyalgorithms.datastructure.trees.bst import TreeNode, BinarySearchTree
from pyalgorithms.datastructure.hashbased.hashtable import HashTable

def test_bst():
    """
    """
    input = lambda: sys.stdin.readline().rstrip()
    print('Enter values separated by comma: ')
    items = list(map(str, input().split(',')))
    print('LENGTH', len(items))
    tree = BinarySearchTree()
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
    if found:
        print('Found ---> ', found.val)
    print('Successor of found: ', tree.successor(found).val)
    print('Predecessor of found: ', tree.predecessor(found).val)
    lines = _build_tree_string(root, 0, False, '')[0]
    print("\n" + "\n".join((line.rstrip() for line in lines)))

    # Validate Binary search tree
    s = Validation()
    result = s.is_valid_bst(root)
    print('Valid: ', result)
    print()

def test_hashtable():
    """
    """
    data = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6),
            ('G', 7), ('H', 8), ('I', 9), ('J', 10), ('K', 11), ('L', 12),
            ('M', 13), ('N', 14), ('O', 15), ('P', 16), ('Q', 17), ('R', 18),
            ('S', 19), ('T', 20), ('V', 21), ('U', 22), ('W', 23), ('X', 24), ('Y', 25), ('Z', 26)]


    ht = HashTable()

    for item in data:
        key, value = item
        ht.insert(key, value)

    print('ADDED', ht.buckets)

    for item in data:
        key, _ = item
        ht.remove(key)

    print('REMOVED', ht.buckets)
    va = ht.get('A')
    print(va)
    print(ht.size_occupied)
    ht.insert('Brian', '28')
    bm = ht.get('BrIaN')
    print(ht.buckets)
    print('Value', bm)
    print(ht.size_occupied)


if __name__ == "__main__":
    test_hashtable()
