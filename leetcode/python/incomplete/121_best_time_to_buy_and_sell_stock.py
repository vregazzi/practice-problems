class Solution:
    def maxProfit2(self, prices: list[int]) -> int:
        minimum = min(prices)
        high = max(prices[prices.index(minimum):])
        return high - minimum

    def maxProfit(self, prices: list[int]) -> int:
        lowest = max(prices)
        for price in prices:
            if price >= lowest:
                continue
            lowest = price

        high = max(prices[prices.index(lowest):])
        if

        return high - lowest
