from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for word in strs:
            check = [0] * 26
            for n in word:
                check[ord(n) - ord("a")] += 1
            a[tuple(check)].append(word)
        
        return list(a.values())
