"""
Parse a linked list from a string
"""
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


def linked_list_from_string(s):
    if s == 'None':
        return None
    data_l = s.split(' -> ')
    data_l = data_l[:-1]
    data_l = [int(el) for el in data_l]
    head = Node(data_l[0])
    current = head
    for data in data_l[1:]:
        current.next = Node(data)
        current = current.next
    return head