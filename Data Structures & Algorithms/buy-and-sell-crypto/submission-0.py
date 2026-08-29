import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxSum = -99999

        while (r<len(prices)):
            if (prices[r] - prices[l] < 0):
                l=r
                r+=1
            else:
                maxSum = max(maxSum, prices[r] - prices[l])
                r+=1
        return maxSum if maxSum > 0 else 0
        