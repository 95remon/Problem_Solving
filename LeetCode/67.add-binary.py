#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        La, Lb = len(a),len(b)
        r, c, t = "", 0, 0
        
        a, b =a[::-1],b[::-1]

        for i in range(max(La,Lb)):
            Da=ord(a[i]) - ord("0") if i<La else 0
            Db=ord(b[i]) - ord("0") if i<Lb else 0
            t= Da+Db+c
            l= str(t%2)
            r = l+r
            c= t//2

        if c:
            r= "1"+r

        return r

        
# @lc code=end

