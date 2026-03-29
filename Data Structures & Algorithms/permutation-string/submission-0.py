class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = {}
        for char in s1:
            store[char] = store.get(char, 0) + 1
        window_store = {}
        for i in range(len(s2)):
            window_store[s2[i]] = window_store.get(s2[i], 0) + 1
            if i >= len(s1):
                window_store[s2[i-len(s1)]] = window_store.get(s2[i-len(s1)], 0) - 1
                if window_store[s2[i-len(s1)]] <= 0:
                    del window_store[s2[i-len(s1)]]
            if window_store == store:
                return True
        return False

            
