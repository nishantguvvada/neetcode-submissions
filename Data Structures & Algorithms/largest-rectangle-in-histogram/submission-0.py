class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area
        # max_area = 0
        # for i in range(0, len(heights)):

        #     j = i
        #     k = i
        #     while j >= 0 and heights[i] <= heights[j]:

        #         j -= 1
        #     while k < len(heights) and heights[i] <= heights[k]:

        #         k += 1
        #     max_area = max(max_area, (k - j - 1) * heights[i])
        # return max_area