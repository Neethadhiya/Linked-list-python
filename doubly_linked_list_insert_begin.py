class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
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
            new_node.prev=current
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

list1=DoublyLinkedList()
list1.insert(1)
list1.insert(7)
list1.insert(2)
print("list before insertion")
list1.display()
list1.insert_beginning(90)
print("list after insertion")
list1.display()


            
            
    
