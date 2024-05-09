# @before-stub-for-debug-begin
from python3problem169 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for n in nums :
            if n in map.keys() :
                map[n] += 1
            else :
                map[n] = 1
        
        for key, value in map.items():
            if value > len(nums)/2 :
                return key
        
# @lc code=end

