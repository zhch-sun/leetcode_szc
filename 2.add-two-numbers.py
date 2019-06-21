#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        next = self.next.__repr__() if self.next is not None else ""
        return str(self.val) + ' , ' + next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = cur = ListNode(0)
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return root.next

if __name__ == '__main__':
    """
    just normal calculation
    can also use a recursive solution
    """
    def list_init(l):
        if len(l) > 0:
            node = ListNode(l[0])
            node.next = list_init(l[1:])
            return node
        else:
            return None

    l1 = list_init([2,4,3])
    l2 = list_init([5,6,4])
    # print(l1.val, l1.next.val, l1.next.next.val)
    s = Solution()
    out = s.addTwoNumbers(l1, l2)
    print(out)
        

