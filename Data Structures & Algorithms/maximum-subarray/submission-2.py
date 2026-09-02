class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #var to keep track of res
        #var for sum which starts at value of left

        #left at the start, right 1

        #right gonna move across each element of nums
        #currentVal gonna add right value

        #if the sum if negative then left gonna move to right + 1

        maxResult = -999
        if len(nums) == 1:
            return nums[0]
        curr = 0
        
        left = 0

        for r in range(len(nums)):
            curr += nums[r]
            maxResult = max(maxResult, curr)
            if curr < 0:
                left = r + 1
                maxResult = max(maxResult, curr)
                curr = 0
        return maxResult