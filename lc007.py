#Given a 32-bit signed integer, reverse digits of an integer. 
#
# Example 1: 
#
# 
#Input: 123
#Output: 321
# 
#
# Example 2: 
#
# 
#Input: -123
#Output: -321
# 
#
# Example 3: 
#
# 
#Input: 120
#Output: 21
# 
#
# Note: 
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. 
# Related Topics Math



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
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
