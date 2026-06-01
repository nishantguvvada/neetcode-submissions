class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def recurse(i, curr_list, curr_sum):

            if curr_sum == target:
                res.append(curr_list.copy())
                return

            if i >= len(nums) or curr_sum > target:
                return

            curr_list.append(nums[i])

            recurse(i, curr_list, curr_sum + nums[i])

            curr_list.pop()

            recurse(i + 1, curr_list, curr_sum)

        recurse(0, [], 0)
        return res