#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s = s + str(i)

        n=str(int(s)+1)

        res=[]

        for j in range(len(n)):
            res.append(int(n[j]))
        
        return res


        
        
# @lc code=end

