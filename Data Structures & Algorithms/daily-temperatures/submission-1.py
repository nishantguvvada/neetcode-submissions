class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # pointer = 0
        # result = []
        # while pointer < len(temperatures):
        #     compare = pointer + 1
        #     while compare <= len(temperatures) - 1 and temperatures[pointer] >= temperatures[compare]:
        #         compare += 1
        #     if compare < len(temperatures):
        #         result.append(compare - pointer)
        #     else:
        #         result.append(0)
        #     pointer += 1
        # return result
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append(i)
        return result