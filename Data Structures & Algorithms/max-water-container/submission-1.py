class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        area = 0
        maxHeights = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l],heights[r])
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
            maxArea = max(area, maxArea)

        return maxArea