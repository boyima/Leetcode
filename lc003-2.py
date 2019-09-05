#Given a string, find the length of the longest substring without repeating characters. 
#
# 
# Example 1: 
#
# 
#Input: "abcabcbb"
#Output: 3 
#Explanation: The answer is "abc", with the length of 3. 
# 
#
# 
# Example 2: 
#
# 
#Input: "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
# 
#
# 
# Example 3: 
#
# 
#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3. 
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# 
# 
# 
# Related Topics Hash Table Two Pointers String Sliding Window



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        curlen = 0
        headind = 0
        charset = set()
        curind = 0
        while curind < len(s):
            curchar = s[curind]
            if curchar not in charset:
                charset.add(curchar)
                curlen += 1
                curind += 1
                maxlen = max(maxlen, curlen)
            else:
                charset.remove(s[headind])
                curlen -= 1
                headind += 1
        return maxlen


        
#leetcode submit region end(Prohibit modification and deletion)
