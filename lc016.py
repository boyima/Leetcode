#Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution. 
#
# Example: 
#
# 
#Given array nums = [-1, 2, 1, -4], and target = 1.
#
#The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# Related Topics Array Two Pointers



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        minDiff = sys.maxsize
        n = len(nums)
        nums.sort()
        i = 0
        while i < n - 2:
            j = i + 1
            k = n - 1
            while j < k:
                curDiff = nums[i] + nums[j] + nums[k] - target
                if curDiff == 0:
                    return target
                if abs(curDiff) < minDiff:
                    minDiff = abs(curDiff)
                    res = curDiff + target
                if curDiff < 0:
                    while j + 1 < k and nums[j] == nums[j + 1]:
                        j = j + 1
                    j = j + 1
                else:
                    while k - 1 > j and nums[k - 1] == nums[k]:
                        k = k - 1
                    k = k - 1
            while i + 1 < n - 2 and nums[i] == nums[i + 1]:
                i = i + 1
            i = i + 1
        return res


#leetcode submit region end(Prohibit modification and deletion)
