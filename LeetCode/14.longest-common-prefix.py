#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# @lc code=start


# strs = ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""
        
        prefix = strs[0]
        for i in range(len(prefix)):
            for str in strs[1:]:
                if (i == len(str) or prefix[i] != str[i]):
                    return prefix[0:i]

        return prefix

# @lc code=end

