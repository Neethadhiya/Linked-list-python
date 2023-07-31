class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete_middle(self, target):
        if self.head is None:
            return  # Empty list, nothing to delete

        current = self.head
        previous = None

        # Traverse the list to find the node to delete
        while current:
            if current.data == target:
                break
            previous = current
            current = current.next

        if current is None:
            return  # Node not found

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

# Create a linked list
my_list = LinkedList()

# Insert some elements into the list
my_list.insert(3)
my_list.insert(7)
my_list.insert(1)
my_list.insert(5)
my_list.insert(9)

print("Original linked list:")
my_list.display()

# Delete the node with value 1 (middle node)
my_list.delete_middle(1)

print("Linked list after deleting the middle node:")
my_list.display()
