#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. 
#
# Note: 
#
# The solution set must not contain duplicate triplets. 
#
# Example: 
#
# 
#Given array nums = [-1, 0, 1, 2, -1, -4],
#
#A solution set is:
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]
# Related Topics Array Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()
        if n < 3:
            return res
        i = 0

        while i < n - 2:
            if nums[i] > 0:
                break
            j = i + 1
            k = n - 1
            while j < k:
                if nums[k] < 0:
                    break
                curSum = nums[i] + nums[j] + nums[k]
                if curSum > 0:
                    while k - 1 > j and nums[k] == nums[k - 1]:
                        k = k - 1
                    k = k - 1
                elif curSum < 0:
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    j = j + 1
                else:
                    curRes = [nums[i], nums[j], nums[k]]
                    res.append(curRes)
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    j = j + 1
            while i + 1 < n - 2 and nums[i] == nums[i + 1]:
                i = i + 1
            i = i + 1
        return res


        
#leetcode submit region end(Prohibit modification and deletion)
