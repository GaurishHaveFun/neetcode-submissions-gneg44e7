class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # adding next element
            subset.append(nums[i])
            dfs(i + 1)

            # dont add next element
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

