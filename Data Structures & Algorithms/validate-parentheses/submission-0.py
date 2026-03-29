class Solution:
    def isValid(self, s: str) -> bool:
        store = {"(":")", "[":"]", "{":"}"}
        cache=[]
        for char in s:
            if char in store.keys():
                cache.append(char)
            else:
                if len(cache) < 1:
                    return False
                if store[cache.pop()] != char:
                    return False

        return len(cache) == 0
        
