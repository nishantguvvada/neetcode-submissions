class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # 2 pointers
        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     if nums[l] + nums[r] > target:
        #         r -= 1
        #     elif nums[l] + nums[r] < target:
        #         l += 1
        #     else:
        #         return [l, r]
        store = {}
        for i, n in enumerate(nums):
            compl = target - n
            if compl in store.keys():
                return [store[compl], i]
            store[n] = i



