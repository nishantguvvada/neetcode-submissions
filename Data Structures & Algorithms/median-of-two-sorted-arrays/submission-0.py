class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2
            j = ((m + n + 1) // 2) - i
            
            left1_max = nums1[i-1] if i > 0 else float('-inf')
            right1_min = nums1[i] if i < m else float('inf')

            left2_max = nums2[j-1] if j > 0 else float('-inf')
            right2_min = nums2[j] if j < n else float('inf')

            if left1_max > right2_min:
                high = i - 1
            elif left2_max > right1_min:
                low = i + 1
            else:
                if (m + n) % 2 == 1:
                    return float(max(left1_max, left2_max))
                else:
                    return (max(left1_max, left2_max) + min(right1_min, right2_min)) / 2.0