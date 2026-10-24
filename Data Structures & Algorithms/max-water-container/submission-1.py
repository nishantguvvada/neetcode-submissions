class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = 0
        # for i in range(len(heights)):
        #     left = i + 1
        #     while left <= len(heights) - 1:
        #         width = left - i
        #         height = min(heights[i], heights[left])
        #         area = max(area, height * width)
        #         left += 1
        # return area
        area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = max(area, height * width)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area