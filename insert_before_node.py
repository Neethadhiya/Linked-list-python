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
    def insert_before(self,before_node,num):
        if self.head is None:
            print("Linked list is empty")
            return
        new_node=Node(num)
        if self.head.data==before_node:
            new_node.next=self.head
            self.head=new_node
            return
        current=self.head
        found=False
        while current.next:
            if current.next.data==before_node:
                found=True
                new_node.next=current.next
                current.next=new_node
                break
            current=current.next
        if not found:
            print("Node not found")
list=LinkedList()
list.insert(10)
list.insert(11)
list.insert(12)
list.insert(13)
print("linked list")
list.display()
before_node=int(input("Enter the node"))
num=int(input("Enter the number to insert"))
list.insert_before(before_node,num)
list.display()