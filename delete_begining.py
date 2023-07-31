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
                temp=temp.next
    def delete_begining(self):
        if self.head is None:
            print("empty")
            return
        else:
            self.head=self.head.next
n1=Node(10)
n2=Node(20)
n3=Node(30)
li= LinkedList()
li.head=n1
n1.next=n2
n2.next=n3
li.delete_begining()
li.display()
