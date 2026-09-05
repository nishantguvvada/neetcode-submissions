class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for el in strs:
            value = ''.join(sorted(el))
            ans[value].append(el)
        return list(ans.values())