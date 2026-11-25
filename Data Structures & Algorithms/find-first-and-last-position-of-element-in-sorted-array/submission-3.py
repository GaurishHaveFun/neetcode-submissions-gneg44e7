class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l,r = 0, len(nums)
        small = -1
        big = -1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                small = mid
                r = mid
        
        l,r = 0, len(nums)
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                big = mid
                l = mid + 1
        
        return [small,big]