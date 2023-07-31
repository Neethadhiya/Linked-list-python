class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node= Node(data)
        if self.head==None:
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
            temp = self.head
            while temp is not None:
                print(temp.data,end=" ")
                temp = temp.next

            print()

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Create a linked list
ll1 = LinkedList()
n1=ll1.insert(11)
n2=ll1.insert(22)
n3=ll1.insert(33)
print("linked list before insertion")
ll1.display()
print("linked list after insertion")
ll1.insert_at_beginning(300)
ll1.display()
