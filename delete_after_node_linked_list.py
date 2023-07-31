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
    def delete_after(self,data):
        if self.head is None:
            print("Linked list is empty")
        else:
            found=False
            current=self.head
            while current:
                if data==current.data:
                    found=True
                    if current.next:
                        current.next=current.next.next
                    else:
                        print("No node after this data")
                current=current.next
            if not found:
                print("data not in the list")
list=LinkedList()
list.insert(10)
list.insert(11)
list.insert(12)
list.insert(13)
list.insert(14)
print("Linked list")
list.display()
num=int(input("Enter the number before to delete"))
print("Linked list after deletion")
list.delete_after(num)
list.display()