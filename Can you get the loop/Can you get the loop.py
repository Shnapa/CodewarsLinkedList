def loop_size(node):
    slow = node
    fast = node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = node
            while fast != slow:
                slow = slow.next
                fast = fast.next
            temp = slow.next
            count = 1

            while temp != fast:
                count += 1
                temp = temp.next
            return count
    return None