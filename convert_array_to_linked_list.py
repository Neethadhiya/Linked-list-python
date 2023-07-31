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
            print("Linked list is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
a=[1,2,3,4,5,6,6]
print("array",a)
list=LinkedList()
for i in range(len(a)):
    list.insert(a[i])
print("array converted to linked list")
list.display()

