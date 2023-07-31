class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
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
        temp= self.head
        if temp is None:
            print("empty")
        else:
            while temp:
                print(temp.data)
                temp=temp.next

    def insert_after(self,prev_node,data):
        if prev_node is None:
            print("Empty linked list")
            return
        else:
            current=self.head
            found=False
            while current:
                new_node = Node(data)
                if current.data==prev_node:
                    found=True
                    new_node.next=current.next
                    current.next=new_node
                    break
                current=current.next
            if not found:
                print("Previous node not fouund")
li= LinkedList()
li.insert(10)
li.insert(20)
li.insert(30)
prev_node=li.head.next
print("list before insertion")
li.display()
prev_node=int(input("Enter the previous node"))
num=int(input("Enter the number to insert"))
li.insert_after(prev_node,num)
print("after insertion")
li.display()
















