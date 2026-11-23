class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        hashMap = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            hashMap[sort].append(word)
        
        for ans in hashMap.values():
            res.append(ans)

        return res