from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        n = len(self.stack)
        self.stack.append(x)
        for _ in range(n):
            self.stack.append(self.stack.popleft())
        

    def pop(self) -> int:
        if self.empty():
            return
        else:
            return self.stack.popleft()

    def top(self) -> int:
        if self.empty():
            return 0
        else: 
            return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()