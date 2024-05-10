#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit :
            visit.add(n)
            n = self.sumOfSquere(n)

            if n == 1 :
                return True

        return False

    def sumOfSquere(self, n: int) -> int:
        output = 0 
        while n:
            d = n % 10
            d = d ** 2
            output += d
            n = n // 10
        
        return output


# @lc code=end

