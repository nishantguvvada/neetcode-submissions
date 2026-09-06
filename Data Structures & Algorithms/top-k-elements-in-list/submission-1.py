class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store = {}
        # for el in nums:
        #     store[el] = store.get(el, 0) + 1
        # result = sorted(store.keys(), key=lambda x: store[x], reverse=True)[:k]
        # return result
        # count = Counter(nums)
        # buckets = [[] for _ in range(len(nums) + 1)]

        # for num, freq in count.items():
        #     buckets[freq].append(num)

        # result = []
        # for i in range(len(buckets) - 1, 0, -1):
        #     for num in buckets[i]:
        #         result.append(num)
        #         if len(result) == k:
        #             return result 
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

