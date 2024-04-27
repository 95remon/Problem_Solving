#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        o, t = 1, 1
        for i in range(n-1):
            temp = o
            o = t+o
            t = temp

        return o
# @lc code=end

