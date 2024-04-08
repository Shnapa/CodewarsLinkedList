"""
Recursive Reverse
"""
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if head is None or head.next is None:
        return head
    part = reverse(head.next)
    head.next.next = head
    head.next = None
    return part 
