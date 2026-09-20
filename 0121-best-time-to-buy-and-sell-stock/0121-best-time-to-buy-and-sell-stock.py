class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min = sys.maxsize
        profit = 0 
        for price in prices:
            if price <min:
                min = price
            profit = max(profit,price - min ) 
        return profit    