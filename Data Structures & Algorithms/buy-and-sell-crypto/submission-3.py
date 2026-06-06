class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP backtrack of highest price and best profit so far
        maximum = prices[-1]
        maximumGap = 0
        for i in range(len(prices)-2, -1, -1):
            maximumGap = max(maximumGap, maximum-prices[i])
            maximum = max(maximum, prices[i])
        return maximumGap


        