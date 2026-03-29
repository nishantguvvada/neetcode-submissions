from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     output.append(product)
        # return output
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        prefix[0] = 1
        suffix[n-1] = 1 
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        return [a * b for a, b in zip(prefix, suffix)]