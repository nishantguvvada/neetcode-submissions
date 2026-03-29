class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # new_len = 2 * len(nums)
        ans = []
        # for i in range(new_len):
        #     # if i > len(nums)-1:
        #     #     index=i-len(nums)
        #     #     ans.append(nums[index])
        #     # else:
        #     #     ans.append(nums[i])
        #     if i > len(nums)-1:
        #         index=i%len(nums)
        #         ans.append(nums[index])
        #     else:
        #         ans.append(nums[i])
        ans = nums + nums
        return ans