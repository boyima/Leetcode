#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward. 
#
# Example 1: 
#
# 
#Input: 121
#Output: true
# 
#
# Example 2: 
#
# 
#Input: -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# 
#
# Example 3: 
#
# 
#Input: 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
#
# Follow up: 
#
# Coud you solve it without converting the integer to a string? 
# Related Topics Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        reversex = self.reverse(x)
        return reversex == x

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        cur = x
        res = 0
        if x < 0:
            cur = -cur
        while cur != 0:
            res = res * 10
            res = res + cur % 10
            cur = cur / 10
        if res > 0x7FFFFFFF:
            return 0
        if x < 0:
            res = -res
        return res
        
#leetcode submit region end(Prohibit modification and deletion)
