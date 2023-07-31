class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.tail = new_node

    def display(self):
        temp = self.head
        if temp is None:
            print("Empty")
        else:
            while temp:
                print(temp.data)
                temp = temp.next

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

dll = DoublyLinkedList()
dll.insert(10)
dll.insert(20)
dll.insert(30)
print("Before insertion:")
dll.display()
print("After insertion:")
dll.insert(30)
dll.insert_end(88)

dll.display()
