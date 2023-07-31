class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.head=None
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
            print("empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def delete_last(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head=None 
            return
        else:
            current=self.head
            while current.next:
                prev=current
                current=current.next
            prev.next=None
                
             
list=LinkedList()
list.insert(10)
list.insert(20)
list.insert(30)
list.insert(40)
list.insert(50)
list.display()
print("after deletion")
list.delete_last()
list.display()  