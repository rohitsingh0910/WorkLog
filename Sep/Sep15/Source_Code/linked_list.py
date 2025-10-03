# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# lis=[10,20,30,40]
# head=Node(lis[0])
# current=head
# for i in lis[1:]:
#     current.next=Node(i)
#     current=current.next
# def traverse(head):
#     current=head
#     while current:
#         print(current.data,end=" -> ")
#         current=current.next
#     print("None")
# traverse(head)
# def reverse(head):
#     prev = None
#     current = head
#     while current:
#         next_node = current.next
#         current.next = prev
#         prev = current
#         current = next_node
#     return prev
#
# head = reverse(head)
# traverse(head)
#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_at_position(head, data, position):
    new_node = Node(data)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    count = 0
    while current and count < position - 1:
        current = current.next
        count += 1
    if current is None:
        return head
    new_node.next = current.next
    current.next = new_node
    return head

def delete_at_beginning(head):
    if not head:
        return head
    return head.next

def delete_at_end(head):
    if not head or not head.next:
        return None
    current = head
    while current.next and current.next.next:
        current = current.next
    current.next = None
    return head

def delete_at_position(head, position):
    if position == 0:
        return head.next
    current = head
    count = 0
    while current and count < position - 1:
        current = current.next
        count += 1
    if current is None or current.next is None:
        return head
    current.next = current.next.next
    return head

lis = [10, 20, 30, 40]
head = Node(lis[0])
current = head
for i in lis[1:]:
    current.next = Node(i)
    current = current.next

print("Original List:")
traverse(head)

head = reverse(head)
print("\nReversed List:")
traverse(head)

head = insert_at_beginning(head, 5)
print("\nAfter Inserting 5 at the Beginning:")
traverse(head)

head = insert_at_end(head, 50)
print("\nAfter Inserting 50 at the End:")
traverse(head)

head = insert_at_position(head, 25, 2)
print("\nAfter Inserting 25 at Position 2:")
traverse(head)

head = delete_at_beginning(head)
print("\nAfter Deleting at the Beginning:")
traverse(head)

head = delete_at_end(head)
print("\nAfter Deleting at the End:")
traverse(head)

head = delete_at_position(head, 2)
print("\nAfter Deleting at Position 2:")
traverse(head)
