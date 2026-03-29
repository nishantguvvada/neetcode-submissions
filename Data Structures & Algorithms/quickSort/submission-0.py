# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        if len(pairs) <= 1:
            return pairs

        pivot = pairs[-1]
        pointer = 0
        for i in range(len(pairs)-1):
            if pairs[i].key < pivot.key:
                temp = pairs[pointer]
                pairs[pointer] = pairs[i]
                pairs[i] = temp
                pointer += 1
        temp = pairs[pointer]
        pairs[pointer] = pivot
        pairs[-1] = temp

        left = self.quickSort(pairs[:pointer])
        right = self.quickSort(pairs[pointer+1:])

        return left + [pivot] + right