#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        next = (',' + self.next.__repr__()) if self.next is not None else ''
        return str(self.val) +  next

class Solution(object):
    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     if l1 and l2:
    #         if l1.val > l2.val:
    #             l1, l2 = l2, l1
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #     return l1 or l2

    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     if not (l1 and l2):
    #         return l1 or l2
    #     if l1.val > l2.val:
    #         l1, l2 = l2, l1
    #     l1.next = self.mergeTwoLists(l1.next, l2)
    #     return l1

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """    
        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            cur.next = l1
            l1 = l1.next 
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

        
if __name__ == '__main__':
    """
    TODO python 支持尾递归吗
    TODO 和第二题一样, 都需要一个dummy root?
    第一个recursion太简单不易懂, 采用第二个recursion. 
    cur和l1 l2必须同时前进..别忘了..
    """
    def singleListInit(l):
        if len(l) == 0:
            return None
        else:
            cur = ListNode(l[0])
            cur.next = singleListInit(l[1:])
            return cur

    s = Solution()
    l1 = singleListInit([1,2])
    l2 = singleListInit([1,3])    
    print(s.mergeTwoLists(l1, l2))

