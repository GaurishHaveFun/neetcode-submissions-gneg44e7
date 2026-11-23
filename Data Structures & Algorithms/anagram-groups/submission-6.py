class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        hashMap = defaultdict(list)
        for word in strs:
            sort = ''.join(sorted(word))
            hashMap[sort].append(word)
        
        

        return list(hashMap.values())