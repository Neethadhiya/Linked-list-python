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
            print("List is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def linear_search(self,data):
        if self.head is None:
            print("Linked list is empty")
        else:
            current=self.head
            index=0
            found=False
            while current:
                if current.data==data:
                    found=True
                    return index+1
                current=current.next
                index+=1
            if found==False:
                return -1
list=LinkedList()
list.insert(10)
list.insert(11)
list.insert(12)
list.insert(14)
list.display()
target=11
index=list.linear_search(target)
if index!=-1:
    print("Position",index)
else:
    print("Number not found")
