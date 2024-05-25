
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head
    
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    sorted_list = merge_sorted_lists(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    dummy = Node()
    tail = dummy

    while left and right:
        if left.value <= right.value:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    if left:
        tail.next = left
    if right:
        tail.next = right

    return dummy.next


def merge_two_sorted_lists(l1, l2):
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next

# Створимо список
llist = LinkedList()
llist.append(3)
llist.append(1)
llist.append(4)
llist.append(2)

print("Original list:")
llist.print_list()

# Реверсування списку
reverse_linked_list(llist)
print("Reversed list:")
llist.print_list()

# Сортування злиттям
llist.head = merge_sort_linked_list(llist.head)
print("Sorted list:")
llist.print_list()

# Об'єднання двох відсортованих списків
llist1 = LinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(5)

llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)

merged_head = merge_two_sorted_lists(llist1.head, llist2.head)
merged_list = LinkedList()
merged_list.head = merged_head

print("Merged sorted list:")
merged_list.print_list()