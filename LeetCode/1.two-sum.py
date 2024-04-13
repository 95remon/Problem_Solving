#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i,n in enumerate(nums) :
            sub = target - n
            if sub in hash_map :
                return [hash_map[sub],i]
            hash_map[n] = i

        return []

# @lc code=end

