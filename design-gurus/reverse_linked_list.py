def reverse(head):
    prev, curr, next = None, head, None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev