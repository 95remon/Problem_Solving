#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            if nums[i] != val:
                nums[c]=nums[i]
                c+=1
        
        return c
# @lc code=end

