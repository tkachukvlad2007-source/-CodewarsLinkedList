from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node is None:
        raise Exception("List is empty")
    i = 0
    current = node
    if index == 0:
        return current

    while current:
        if index == i:
            return current
        i+=1
        current = current.next

    raise Exception("Index out of range")
