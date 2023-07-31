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
    def remove_duplicates(self):
        if self.head is None:
            print("list is empty")
        current=self.head
        unique=[]
        index=0
        while current.next:
            print(current.data,index+1)
            if current.data in unique:
                current=current.next
            else:
                unique.append(current.data)
                current=current.next
        return unique

li =LinkedList()
li.insert(10)
li.insert(20)
li.insert(21)
li.insert(21)
li.insert(23)

li.insert(30)
li.display()
unique=li.remove_duplicates()
print(unique)