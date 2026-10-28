class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recurse(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return recurse(left, mid - 1)
            else:
                return recurse(mid + 1, right)
            
        return recurse(0, len(nums) - 1)
        # start = 0
        # end = len(nums) - 1
        # while start <= end:
        #     mid = (start + end) // 2
        #     if nums[mid] == target:
        #         return mid
        #     if nums[mid] > target:
        #         end = mid - 1
        #     else:
        #         start = mid + 1
        # return -1