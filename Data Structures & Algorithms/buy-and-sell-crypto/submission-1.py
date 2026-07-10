class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        bestprofit = 0

        for p in prices:
            minBuy = min(minBuy, p)
            bestprofit = max(bestprofit, p-minBuy)
        return bestprofit
        