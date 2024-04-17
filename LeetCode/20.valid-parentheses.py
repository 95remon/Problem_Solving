#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { 
            '(':')',
            '{':'}',
            '[':']',
        }
        
        for b in s :
            if b in brackets :
                stack.append(b)
            elif len(stack) == 0 or b != brackets[stack.pop()]:
                return False

        return len(stack) == 0

# @lc code=end

