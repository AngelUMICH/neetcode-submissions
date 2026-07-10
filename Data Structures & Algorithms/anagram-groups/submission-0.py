class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i,s in enumerate(strs):
            sorted_key = ''.join(sorted(s))
            seen[sorted_key].append(s)
        return list(seen.values())

        