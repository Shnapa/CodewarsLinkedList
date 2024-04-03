"""
Convert a linked list to a string
"""
def stringify(node):
    if not node:
        return 'None'
    res = []
    temp = node
    while temp:
        res.append(str(temp.data))
        temp = temp.next
    return ' -> '.join(res) + ' -> None'