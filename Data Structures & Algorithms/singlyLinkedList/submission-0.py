class Node:

    def __init__(self, value=0):
        self.next = None
        self.value = value

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1

        curr = self.head
        i = 0
        while i < index:
            if not curr.next:
                return -1
            curr = curr.next
            i += 1
        return curr.value

    def insertHead(self, val: int) -> None:
        new_node = Node(value=val)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(value=val)
        if not self.tail:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            if self.head.next is None:
                self.tail = None
            self.head = self.head.next
            return True
        
        curr = self.head
        i = 0
        while i < index - 1:
            if curr.next is None:
                return False

            curr = curr.next
            i += 1
        if curr.next is None:
            return False
            
        if curr.next == self.tail:
            self.tail = curr

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next

        return result