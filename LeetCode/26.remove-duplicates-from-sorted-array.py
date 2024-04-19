#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        Lp = 0

        for Rp in range(1,n):
            if nums[Rp] != nums[Lp]:
                nums[Lp+1]=nums[Rp]
                Lp += 1
        
        return Lp+1
        
# @lc code=end

