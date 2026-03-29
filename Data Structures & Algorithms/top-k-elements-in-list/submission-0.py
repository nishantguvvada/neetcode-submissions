class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for i in nums:
            store[i] = store.get(i, 0) + 1
        result = [k for k, v in sorted(store.items(), key=lambda x: x[1], reverse=True)]
        return result[:k]