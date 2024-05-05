# @before-stub-for-debug-begin
from python3problem125 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS = ""
        for c in s :
            if c.isalnum():
                newS += c.lower()
             

        return newS == newS[::-1]
            
# @lc code=end

