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
    def delete_value(self,data):
        if self.head is None:
            print("Linked list is empty")
        elif self.head==data:
            self.head=self.head.next
        else:
            current=self.head
            found =False
            while current.next:
                if current.next.data==data:
                    found=True
                    current.next=current.next.next
                    break
                current=current.next
            if not found:
                print("Number not in the linked list")
list=LinkedList()
list.insert(10)
list.insert(11)
list.insert(12)
list.insert(13)
print("Linked list")
list.display()
num=int(input("Enter the value to delete"))
list.delete_value(num)
print("Linked list after deletion")
list.display()            