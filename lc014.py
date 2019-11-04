#Write a function to find the longest common prefix string amongst an array of strings. 
#
# If there is no common prefix, return an empty string "". 
#
# Example 1: 
#
# 
#Input: ["flower","flow","flight"]
#Output: "fl"
# 
#
# Example 2: 
#
# 
#Input: ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
# 
#
# Note: 
#
# All given inputs are in lowercase letters a-z. 
# Related Topics String



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ""
        if len(strs) == 0:
            return lcp
        minLen = len(strs[0])
        for i in range(len(strs)):
            minLen = min(minLen, len(strs[i]))
        isCp = True
        for i in range(minLen):
            if not isCp:
                break
            for j in range(len(strs)):
                if strs[j][i] == strs[0][i]:
                    continue
                else:
                    isCp = False
                    break
            if isCp:
                lcp = lcp + strs[0][i]
        return lcp

#leetcode submit region end(Prohibit modification and deletion)
