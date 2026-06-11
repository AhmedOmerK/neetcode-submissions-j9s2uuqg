class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        left = 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                curr = prices[right] - prices[left]
                maxprof = max(maxprof, curr)
        return maxprof