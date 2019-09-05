#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. 
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself. 
#
# Example: 
#
# 
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
# 
# Related Topics Linked List Math



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curNode = dummy
        carry = 0
        n1 = l1
        n2 = l2
        while n1 is not None or n2 is not None or carry is not 0:
            curSum = 0
            if n1 is not None:
                curSum += n1.val
                n1 = n1.next
            if n2 is not None:
                curSum += n2.val
                n2 = n2.next
            curSum += carry
            carry = curSum / 10
            curNode.next = ListNode(curSum % 10)
            curNode = curNode.next
        return dummy.next


        
#leetcode submit region end(Prohibit modification and deletion)
