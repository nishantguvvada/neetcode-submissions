class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # store = {}
        # for i in nums:
        #     store[i] = store.get(i, 0) + 1
        # for k, v in store.items():
        #     if v >= 2:
        #         return True
        # return False
        # sorted_arr = sorted(nums)
        # i = 1
        # store = 0
        # while i < len(sorted_arr):
        #     if sorted_arr[store] == sorted_arr[i]:
        #         return True
        #     i += 1
        #     store += 1
        # return False
        return len(nums) != len(set(nums))