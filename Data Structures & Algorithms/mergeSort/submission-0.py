# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def merge(arr, s, m, e):
            left = arr[s:m+1]
            right = arr[m+1:e+1]
            left_pointer = 0
            right_pointer = 0
            result = []

            while left_pointer <= len(left) - 1 and right_pointer <= len(right) - 1:
                if left[left_pointer].key <= right[right_pointer].key:
                    result.append(left[left_pointer])
                    left_pointer += 1
                else:
                    result.append(right[right_pointer])
                    right_pointer += 1
            result += left[left_pointer:]
            result += right[right_pointer:]
            
            for i in range(len(result)):
                arr[s + i] = result[i]
            return arr
 
        def rec_merge(arr, s , e):
            if e - s + 1 <= 1:
                return arr

            m = (s + e) // 2
            rec_merge(arr, s, m)
            rec_merge(arr, m+1, e)

            return merge(arr, s, m, e)

        return rec_merge(pairs, 0, len(pairs) - 1)
