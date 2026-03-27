from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    new_node = Node(data)
    new_node.next = head

    return new_node

def build_one_two_three():
    start = None
    for i in range(3,0,-1):
        new_head = push(start,i)
        start = new_head
    return new_head
