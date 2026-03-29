class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # writer = 0
        # for i in range(0, len(nums)):
        #     if nums[i] != val:
        #         nums[writer] = nums[i]
        #         writer += 1
        # return writer
        first = 0
        last = len(nums) - 1
        while first <= last:
            if nums[first] == val:
                if nums[last] != val:
                    nums[first], nums[last] = nums[last], nums[first]
                    first += 1
                    last -= 1
                else:
                    last -= 1
            else:
                first += 1
        return first
            


