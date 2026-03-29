class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            self.minimum.append(min(val, self.minimum[-1]))
        

    def pop(self) -> None:
        self.arr.pop()
        self.minimum.pop()

    def top(self) -> int:
        if self.arr:
            return self.arr[-1]
        else:
            raise "Stack is empty"

    def getMin(self) -> int:
        print(self.arr)
        print(self.minimum)
        return self.minimum[-1]
