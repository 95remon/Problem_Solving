#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        
        while l <= r :
            m = (l + r) // 2
            if nums[m] > target :
                r = m - 1
            elif nums[m] < target :
                l = m + 1
            else :
                return m
            
        return l

        
        
        
        # n = len(nums)
        # res=0
        # for i in range(n):
        #     if nums[i]==target:
        #         res=i
        #     elif nums[i]<target:
        #         res=i+1
        # return res
# @lc code=end

