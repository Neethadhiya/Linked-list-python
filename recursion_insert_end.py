# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
 
#     def display(self):
#         if self.head is None:
#             print("Linked list is empty")
#         else:
#             temp = self.head
#             while temp is not None:
#                 print(temp.data,end=" ")
#                 temp = temp.next

#             print()

#     # def insert_at_beginning(self, data):
#     #     new_node = Node(data)
#     #     new_node.next = self.head
#     #     self.head = new_node

#     # def insertEnd(self,head, data):
#     #     if self.head == None:
#     #         return Node(data)
#     #     else:
#     #         head.next = self.insertEnd(head.next, data)
#     #     return head
#     def insertEnd(self,head,data):
#         if self.head==None:
#             self.head=Node(data)
#         else:
#             head.next=self.insertEnd(head.next,data)
    
# # Create a linked list
# ll1 = LinkedList()
# print("linked list before insertion")
# ll1.display()
# ll1.insertEnd(ll1.head, 3)
# ll1.insertEnd(ll1.head, 4)
# ll1.insertEnd(ll1.head, 5)
# ll1.insertEnd(ll1.head, 6)
# ll1.insertEnd(ll1.head, 7)

# ll1.display()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
 
    def display(self):
        
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def insertEnd(self, head, data):
        if head is None:
            return Node(data)
        else:
            head.next = self.insertEnd(head.next, data)
            print(data,"next")
            return head
ll1 = LinkedList()

ll1.head = ll1.insertEnd(ll1.head, 3)
print(ll1.head)
ll1.head = ll1.insertEnd(ll1.head, 4)
print(ll1.head)
ll1.head = ll1.insertEnd(ll1.head, 5)
print(ll1.head)
ll1.head = ll1.insertEnd(ll1.head, 6)
print(ll1.head)
ll1.head = ll1.insertEnd(ll1.head, 7)
print(ll1.head)
print("Linked list")
ll1.display()

