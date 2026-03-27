from preloaded import Node

def swap_pairs(head):
    dummy = Node(head)
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    return dummy.next
