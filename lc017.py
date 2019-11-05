#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. 
#
# 
#
# Example: 
#
# 
#Input: "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
#
# Note: 
#
# Although the above answer is in lexicographical order, your answer could be in any order you want. 
# Related Topics String Backtracking



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keyPad = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        padLen = []
        for str in keyPad:
            padLen.append(len(str))
        res = []
        if digits == "":
            return res
        for i in keyPad[ord(digits[0]) - ord('2')]:
            res.append(i)
        for i in range(1, len(digits)):
            curResSize = len(res)
            for j in range(curResSize):
                for k in keyPad[ord(digits[i]) - ord('2')]:
                    res.append(res[j] + k)
            res = res[curResSize:]
        return res

#leetcode submit region end(Prohibit modification and deletion)
