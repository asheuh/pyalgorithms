class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        head = self.head
        while head:
            count += 1
            head = head.next
        return count

    def add_node_end(self, value):
        temp = Node(value=value)

        if not self.head:
            self.head = temp
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = temp

    def add_node_beginning(self, value):
        temp = Node(value=value)
        temp.next = self.head
        self.head = temp

    def in_between(self, existing_node, value):
        node = Node(value=value)
        if not existing_node:
            return

        node.next = existing_node.next
        existing_node.next = node

    def remove(self, key):
        head = self.head

        if head and head.value == key:
            self.head = head.next
            head = None
            return

        while head:
            if head.value == key:
                break
            prev = head
            head = prev.next

        if not head:
            return

        prev.next = head.next
        head = None

    def traverse(self):
        result = []
        node = self.head
        while node:
            result.append(node.value)
            node = node.next
        return result

    def remove_last(self):
        head = self.head
        if not head:
            return

        if not head.next:
            head = None
            return

        while head.next.next:
            head = head.next
        head.next = None


if __name__ == '__main__':
    sll = SinglyLinkedList()
    items = [12, 13, 14, 15, 16, 17, 18, 19, 20]
    for item in items:
        sll.add_node_end(item)
    print(sll.traverse())
    sll.remove(15)
    sll.remove(20)
    sll.in_between(sll.head.next.next, 15)
    print(sll.traverse())
    print(len(sll))
    sll.remove_last()
    print(sll.traverse())

