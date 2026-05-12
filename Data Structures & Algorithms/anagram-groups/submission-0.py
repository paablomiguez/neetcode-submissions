from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            canonical = "".join(sorted(s))
            groups[canonical].append(s)
        return list(groups.values())