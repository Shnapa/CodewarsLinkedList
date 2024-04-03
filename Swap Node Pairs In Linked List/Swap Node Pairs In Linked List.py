class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    new = head.next
    while head and head.next:
        first = head
        second = head.next
        first.next = second.next
        second.next = first
        if first.next and first.next.next:
            first.next = first.next.next
        head = first.next
    return new