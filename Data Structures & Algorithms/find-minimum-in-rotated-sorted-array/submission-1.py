class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Clues 4 and 6, 4 moves the last 4 elements to beginning, 6 produces original
        # No need to worry about duplicates in the array
        # Binary Search = log n time
        # Also searching for a "min" which points to binary search
        # but binary search needs sorting, we need to reverse the rotation
        # but we are not given how many times it is rotated
        # 1) 6,1,2,3,4,5 , 2) 5,6,1,2,3,4 , 3) 4,5,6,1,2,3 4) 3,4,5,6,1,2
        # rotation just means shift all elements
        # rotation bounds = 1 <= rotation <= n 
        # Binary search continuously searches mid point until finding solution
        # last element > first element = min  = first index
        # Binary search helps find the cut

        l, r = 0, len(nums) - 1

        if nums[0] < nums[-1]:
            return nums[0]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[0]:
                r = mid
            else: 
                l = mid + 1
        
        return nums[l]
        