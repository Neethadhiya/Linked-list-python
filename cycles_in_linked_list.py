# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# def has_cycle(head):
#     if not head or not head.next:
#         return False

#     tortoise = head
#     hare = head.next

#     while tortoise != hare:
#         if not hare or not hare.next:
#             return False
#         tortoise = tortoise.next
#         hare = hare.next.next

#     return True

# # Test case 1: A linked list with a cycle
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = head.next  # Create a cycle

# print(has_cycle(head))  # Output: True

# # Test case 2: A linked list without a cycle
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

# print(has_cycle(head))  # Output: False
