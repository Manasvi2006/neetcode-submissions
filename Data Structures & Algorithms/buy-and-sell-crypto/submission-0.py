class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 #where left is buying and right is sell
        maxProfit = 0

        while right < len(prices):
            #is this profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right

            right += 1
        return maxProfit

                

        