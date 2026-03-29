class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            length = right - left
            area = max(area, height * length)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1
                right -= 1
        return area