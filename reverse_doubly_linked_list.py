class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def reverse(self):
        current = self.head
        temp = None

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

# Create a doubly linked list
dll = DoublyLinkedList()
dll.insert(11)
dll.insert(22)
dll.insert(33)

print("Doubly linked list before reversal:")
dll.display()

dll.reverse()

print("Doubly linked list after reversal:")
dll.display()
