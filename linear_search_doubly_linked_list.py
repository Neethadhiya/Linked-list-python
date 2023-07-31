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
            print("Linked list is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def linear_search(self,data):
        if self.head is None:
            print("Linked list is empty")
        else:
            index=0
            current=self.head
            found=False
            while current:
                if data==current.data:
                    found=True
                    return index+1
                current=current.next
                index+=1
            if found==False:
                return -1
list=DoublyLinkedList()
list.insert(11)
list.insert(12)
list.insert(13)
list.insert(15)
list.display()
target=15

index=list.linear_search(target)
if index!=-1:
    print("position",index)
else:
    print("Number not found")