#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000. 
#
# Example 1: 
#
# 
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.
# 
#
# Example 2: 
#
# 
#Input: "cbbd"
#Output: "bb"
# 
# Related Topics String Dynamic Programming



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxlen = 0
        maxbegin = 0
        dparray = [[False for j in range(n)] for i in range(n)]
        for j in range(n):
            for i in range(j + 1):
                dparray[i][j] = (s[i] == s[j]) and ((j - i) <= 2 or dparray[i + 1][j - 1])
                if dparray[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    maxbegin = i
        return s[maxbegin: maxbegin + maxlen]
        
#leetcode submit region end(Prohibit modification and deletion)
