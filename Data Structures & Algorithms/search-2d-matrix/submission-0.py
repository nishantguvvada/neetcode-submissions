class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        first = 0
        last = (m * n) - 1

        while first <= last:
            mid = (first + last + 1) // 2
            if target > matrix[mid // n][mid % n]:
                first = mid + 1
            elif target < matrix[mid // n][mid % n]:
                last = mid - 1
            else:
                return True
        return False