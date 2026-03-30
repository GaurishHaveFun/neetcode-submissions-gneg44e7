class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i in range(len(strs)):
            sortStr = ''.join(sorted(strs[i]))
            anagrams[sortStr].append(strs[i])
        return list(anagrams.values())