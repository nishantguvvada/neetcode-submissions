class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        curr_min = self.min_stack[-1] if self.min_stack else val
        self.min_stack.append(min(val, curr_min))

    def pop(self) -> None:
        self.arr.pop(-1)
        self.min_stack.pop(-1)

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
