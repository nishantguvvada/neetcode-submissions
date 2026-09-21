class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        self.curr = new_node
        

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps = steps - 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps = steps - 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)