from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    parts = list_repr.split(' -> ')
    head = Node(int(parts[0]))
    current = head
    for val in parts[1:-1]:
        current.next = Node(int(val))
        current = current.next
    return head
