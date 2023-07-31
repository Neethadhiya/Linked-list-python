class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        temp = self.head
        if temp is None:
            print("empty")
        else:
            while temp:
                print(temp.data)
                temp = temp.next

li=LinkedList()
n1=Node(10)
n2=Node(11)
n3=Node(12)
li.head=n1
n1.next=n2
n2.next=n3

li.display()       