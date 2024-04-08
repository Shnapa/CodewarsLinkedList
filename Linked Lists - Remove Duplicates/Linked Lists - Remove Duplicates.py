"""
Remove duplicates
"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    cur = head
    while cur:
        while cur.next:
            if cur.next.data == cur.data:
                cur.next = cur.next.next
            else:
                cur = cur.next
        cur = cur.next
    return head
