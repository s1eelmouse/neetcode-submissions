from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        kal = defaultdict(list)
        for i in strs:
            kal[tuple(sorted(i))].append(i)
        return list(kal.values())