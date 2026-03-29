class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sorted_piles = sorted(piles)
        left = 1
        right = max(piles)
        min_k = right

        def compute(k):
            result = []
            for i in range(len(sorted_piles)):
                if sorted_piles[i] % k > 0:
                    val = (sorted_piles[i] // k) + 1
                    result.append( val)
                else:
                    val = sorted_piles[i] // k
                    result.append(val)

            return sum(result)

        while left <= right:

            mid = (left + right) // 2
            if mid == 0: 
                left = 1
                continue

            time = compute(mid)

            if time > h:
                left = mid + 1
            else:
                min_k = mid
                right = mid - 1

        return min_k