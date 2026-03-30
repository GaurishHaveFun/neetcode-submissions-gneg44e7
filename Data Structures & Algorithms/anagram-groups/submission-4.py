class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            newStr = ''.join(sorted(word))
            hashMap[newStr].append(word)
        return list(hashMap.values())