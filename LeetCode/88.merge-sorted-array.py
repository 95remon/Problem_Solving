# @before-stub-for-debug-begin
from python3problem88 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1L = len(nums1)-1
        nums2L = len(nums2)-1

        Last = (m + n) - 1
        while m > 0 and n > 0 :
            i, j = nums1[m-1], nums2[n-1]
            if i > j :
                nums1[Last] = i
                m -= 1 
            else :
                nums1[Last] = j
                n -= 1
            Last -= 1
        while n > 0 :
            nums1[Last] = nums2[n - 1]
            n, Last = n - 1, Last - 1
        
# @lc code=end

