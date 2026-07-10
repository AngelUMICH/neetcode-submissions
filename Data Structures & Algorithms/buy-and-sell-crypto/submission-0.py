class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i,buy in enumerate(prices):
            if i == len(prices)-1:
                return maxprofit
            for sell in prices[i+1:]:
                sellnowprofit = sell - buy
                if (sellnowprofit > maxprofit):
                    maxprofit = sellnowprofit

        return maxprofit

        