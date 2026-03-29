"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {}
        store[None] = None
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            store[curr] = new_node
            curr = curr.next

        curr = head
        while curr:
            new_node = store[curr]
            new_node.next = store.get(curr.next)
            new_node.random = store.get(curr.random)
            curr = curr.next


        return store.get(head)