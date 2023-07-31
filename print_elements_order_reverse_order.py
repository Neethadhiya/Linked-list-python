class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def reverse(self):
        if self.head is None:
            print("Linked list is empty")
            return
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
list=LinkedList()
list.insert(10)
list.insert(11)
list.insert(12)
list.insert(13)
print("Linked list in order")
list.display()
print("Linked list in reverse order")
list.reverse()
list.display()