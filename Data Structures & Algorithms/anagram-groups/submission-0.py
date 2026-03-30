class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for str in strs:
            sorted_string = "".join(sorted(str))
            if sorted_string not in hashMap:
                hashMap[sorted_string] = [str]
            else:
                hashMap[sorted_string].append(str)
        return list(hashMap.values())


