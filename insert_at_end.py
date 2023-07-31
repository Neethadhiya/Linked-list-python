class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.tail = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node= Node(data)
        if self.head == None:
            self.head=new_node
            new_node.tail=None
        else:
            current=self.head
            while current.next:
                current=current.next
            new_node.tail=None
            current.next=new_node
    def display(self):
        temp=self.head
        if temp is None:
            print("empty")
        else:
            while temp:
                print(temp.data)
                temp = temp.next
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head= new_node
            return 
        else:       
            self.tail.next=new_node
            # new_node.next = None
            self.tail=new_node

li =LinkedList()
li.insert(10)
li.insert(20)
li.insert(30)
print("before insertion")
li.display()
print("after insertion")
li.insert_end(88)
li.display()

        

