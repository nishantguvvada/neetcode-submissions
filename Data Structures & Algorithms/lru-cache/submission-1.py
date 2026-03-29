class Node:

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} 
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.make_recent(node)
            return node.value
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.make_recent(node)
        else:
            if len(self.cache) == self.cap:
                lru = self.tail.prev
                del self.cache[lru.key]
                self.remove_node(lru)
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.make_recent(new_node)
            

    def make_recent(self, node):

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node