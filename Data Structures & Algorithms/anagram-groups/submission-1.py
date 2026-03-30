class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for i in range(len(strs)):
            sortStr = ''.join(sorted(strs[i]))
            hashMap[sortStr].append(strs[i])
        return list(hashMap.values())
