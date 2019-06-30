#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """
    #     if not headA or not headB:
    #         return None
    #     pA = headA
    #     pB = headB
    #     while pA is not pB:  # this condition!
    #         pA = pA.next if pA else headB
    #         pB = pB.next if pB else headA
    #     return pA

    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        pA = headA
        pB = headB
        while pA or pB:  # this condition!
            if pA is pB:
                return pA
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return None

if __name__ == '__main__':
    """
    答案有个图示n中情况..非常精巧.. A+B=B+A
    数学证明的话: common+Aspecific  common+Bspecific
    """
    s = Solution()
