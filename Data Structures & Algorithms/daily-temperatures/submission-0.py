class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for idx, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                popped_idx = stack.pop()
                diff = idx - popped_idx                
                result[popped_idx] = diff
            stack.append(idx)
        return result