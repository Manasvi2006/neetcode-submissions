class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        area = 0
        left, right = 0, len(heights)-1
        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                left += 1

            currMax = max(currMax, area)

        return currMax
        