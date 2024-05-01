#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l<=r :
            m = (l + r) // 2
            if (m * m) < x :
                l = m+1
            elif (m * m) > x :
                r = m-1
            else :
                return m

        return r
# @lc code=end

