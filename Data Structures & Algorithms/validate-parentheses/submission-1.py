class Solution:
    def isValid(self, s: str) -> bool:
        store = { "[":"]", "(":")", "{":"}" }
        stack = []
        for el in s:
            if el in store.keys():
                stack.append(el)
            else:
                if not stack or el != store[stack.pop()]:
                    return False
        return not stack
