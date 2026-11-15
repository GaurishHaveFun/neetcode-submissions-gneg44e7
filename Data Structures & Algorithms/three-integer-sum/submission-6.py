class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        nums.sort()
        
        for l in range(len(nums) - 2):
            if nums[l] > 0:
                break
            if l > 0 and nums[l] == nums[l - 1]:
                continue

            m,r = l + 1, len(nums) - 1
            while m < r:
                total = nums[m] + nums[r] + nums[l]
                if total > 0:
                    r -= 1
                elif total < 0:
                    m += 1
                else:
                    arr.append([nums[l],nums[m],nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m - 1]:
                        m += 1
        
        return arr

