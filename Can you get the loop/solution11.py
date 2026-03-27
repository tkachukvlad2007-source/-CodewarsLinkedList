def loop_size(node):
    slow = node
    fast = node
    while True:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break

    count = 1
    current = slow.next
    while  current!=slow:
        current = current.next
        count+=1
    return count
