class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or head.next is None:
        raise ValueError

    first_head = first_end = head
    second_head = head.next
    second_end = second_head

    while first_end and second_end and second_end.next:
        first_end.next = second_end.next
        first_end = first_end.next

        second_end.next = first_end.next
        second_end = second_end.next

    if first_end:
        first_end.next = None

    return Context(first_head, second_head)
