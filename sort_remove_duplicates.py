class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def display(self):
        temp = self.head
        if temp is None:
            print("Empty")
        else:
            while temp:
                print(temp.data)
                temp = temp.next
    def sort(self):
        if self.head is None or self.head.next is None:
            return

        # Selection sort on the linked list
        current = self.head
        while current.next:
            min_node = current
            next_node = current.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next

            current.data, min_node.data = min_node.data, current.data
            current = current.next

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

li = LinkedList()
li.insert(30)
li.insert(20)
li.insert(10)
li.insert(30)
li.insert(20)
print("List before removing duplicates:")
li.display()

li.sort()
li.remove_duplicates()
print("List after removing duplicates:")
li.display()
