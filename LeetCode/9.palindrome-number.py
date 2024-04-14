#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        s = 0
        e = len(num) - 1
        while s <= e : 
            if num[s] != num[e] :
                return False
            s += 1
            e -= 1
        
        return True
        
# @lc code=end

