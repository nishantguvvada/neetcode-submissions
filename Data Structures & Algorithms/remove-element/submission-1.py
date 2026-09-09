class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for i in nums:
            if i != val:
                nums[write] = i
                write += 1
        return write