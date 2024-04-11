#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#


# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0 
        for n in nums :
            if len(str(n))%2 == 0 :
                ans += 1

        return ans
# @lc code=end

