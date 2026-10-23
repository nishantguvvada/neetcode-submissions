class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        q = deque()
        total = 0
        for num in tokens:
            if num in operators:
                b = q.popleft()
                a = q.popleft()
                if num == "+":
                    total = a + b
                if num == "-":
                    total = a - b
                if num == "*":
                    total = a * b
                if num == "/":
                    total = int(a / b)
                q.appendleft(total)
            else:
                q.appendleft(int(num))
        return q[0]

                
