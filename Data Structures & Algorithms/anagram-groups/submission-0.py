from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))

            store[sorted_word].append(word)

        return [values for values in store.values()]

