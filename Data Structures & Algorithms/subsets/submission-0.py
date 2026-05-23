class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def recurse(index, path):
            result.append(list(path))
            for i in range(index, len(nums)):
                path.append(nums[i])
                recurse(i+1, path)
                path.pop()

        recurse(0, [])
        return result
                


            