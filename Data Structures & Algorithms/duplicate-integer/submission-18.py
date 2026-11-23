class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        
        for num in nums:
            if num in hashMap:
                return True
            hashMap.add(num)
        
        return False
        
        
        # nums = [1, 2, 3, 3]

        # if i in hashMap:
        #     return False
            