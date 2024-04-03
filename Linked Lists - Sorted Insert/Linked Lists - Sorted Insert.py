class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    new_node = Node(data)
    if not head or data < head.data:
        new_node.next = head
        return new_node
    cur = head
    while cur.next and cur.next.data < data:
        cur = cur.next
    new_node.next = cur.next
    cur.next = new_node
    return head