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
            print("empty")
        else:
            while temp:
                print(temp.data)
                temp = temp.next

    def linearSearch(self, head, key, position):
        if head is None:
            return -1
        if head.data == key:
            return position+1
        return self.linearSearch(head.next, key, position + 1)
li = LinkedList()
li.insert(10)
li.insert(20)
li.insert(30)

print("List before insertion:")
li.display()
key = 20
position = li.linearSearch(li.head, key, 0)
if position != -1:
    print(f"{key} is found at position {position} in the linked list.")
else:
    print(f"{key} is not found in the linked list.")
