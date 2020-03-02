"""
Import
"""
from binarysearchtree import BinarySearchTree


def main():
    """
    Main function
    """
    node = BinarySearchTree()
    arr = [21, 26, 30, 9, 4, 14, 28, 18, 15, 10, 2, 3, 7]
    for _, value in enumerate(arr):
        node.add(value)

    print(node.preorder(node.root))
    print(node.height())


if __name__ == "__main__":
    main()
