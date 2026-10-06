class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1 #bc you can't buy and sell on same day
        currMax = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            
            if prices[right] - prices[left] >= 0:
                currMax = max(currMax, prices[right] - prices[left])
            
            right += 1
        return currMax

        