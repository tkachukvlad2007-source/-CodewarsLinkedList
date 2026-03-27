class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("Error")

    first = head
    second = head.next

    current_first = first
    current_second = second

    current = head.next.next

    while current:
        current_first.next = current
        current_first = current_first.next
        current = current.next

        if current:
            current_second.next = current
            current_second = current_second.next
            current = current.next

    current_first.next = None
    current_second.next = None

    return Context(first, second)
