#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        return str(self.val) + (', ' + self.next.__repr__() \
            if self.next else '')

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        carry = 0
        cur = dummy = ListNode(None)
        while l1 or l2 or carry:  # carry放在这里更方便
            i = l1.val if l1 else 0
            j = l2.val if l2 else 0
            carry, val = divmod(i + j + carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None  # Note 忘记了!
            l2 = l2.next if l2 else None
        return dummy.next
        
if __name__ == '__main__':
    """
    题设: 链表本身就逆序 445题链表是正序
    坑: 
        一个0, 0 + 0
    """
    def list2node(l):
        cur = dummy = ListNode(0)
        for item in l:
            cur.next = ListNode(item)
            cur = cur.next
        return dummy.next

    s = Solution()
    print(s.addTwoNumbers(list2node([2,4,3]), list2node([5,6,4])))

