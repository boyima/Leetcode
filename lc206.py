#Reverse a singly linked list. 
#
# Example: 
#
# 
#Input: 1->2->3->4->5->NULL
#Output: 5->4->3->2->1->NULL
# 
#
# Follow up: 
#
# A linked list can be reversed either iteratively or recursively. Could you implement both? 
# Related Topics Linked List



#leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next is not None:
            move = cur.next
            cur.next = move.next
            move.next = dummy.next
            dummy.next = move
        return dummy.next

        
#leetcode submit region end(Prohibit modification and deletion)
