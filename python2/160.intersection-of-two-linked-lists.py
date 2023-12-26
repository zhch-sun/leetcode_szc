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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None  # 不需要这一句, 但是可以加快
        pA = headA  # 必须赋值, 因为headA必须保留...
        pB = headB
        while pA is not pB:  # 包含不相交的情况
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

if __name__ == '__main__':
    """
    题设: 找到交点, 没有返回None
    解法:
        答案有个图示n种情况..非常精巧.. A+B=B+A
        数学证明的话: common+Aspecific  common+Bspecific
        坑: 
    """
    s = Solution()
