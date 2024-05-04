#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        maxP = 0

        while R < len(prices):
            if prices[L] < prices [R]:
                maxP = max(maxP, prices[R]- prices[L])
            else:
                L = R
            R += 1
        
        return maxP
# @lc code=end

