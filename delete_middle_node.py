class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def display(self):
        if self.head is None:
            print("emoty")
        else:
            current= self.head
            while current:
                print(current.data)
                current=current.next
    def delete_middle(self):
        if self.head is None or self.head.next is None:
            return
        slow_ptr = self.head
        fast_ptr = self.head
        prev = None
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        if prev:
            prev.next = slow_ptr.next
        else:
            self.head = slow_ptr.next
list=LinkedList()
list.insert(10)
# list.insert(30)
# list.insert(60)
list.insert(690)

print("before deletion")
list.display()
list.delete_middle()
print("after deletion")
list.display()

    