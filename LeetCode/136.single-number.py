# @before-stub-for-debug-begin
from python3problem136 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res_dict = {}
        for n in nums:
            if n not in res_dict.keys() :
                res_dict[n] = 1
            else :
                res_dict[n] = 2

        for key, value in res_dict.items():
            if value == 1  : return key 
        


        
# @lc code=end

