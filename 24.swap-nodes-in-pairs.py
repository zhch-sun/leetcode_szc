#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 96%
        dummy = pre = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next = b
            a.next = b.next
            b.next = a
            pre = a
        return dummy.next
        
    def swapTriple(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 96%
        dummy = pre = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next and pre.next.next.next:
            a = pre.next
            b = a.next
            c = b.next
            pre.next = c
            a.next = c.next
            c.next = b
            b.next = a
            pre = a
        return dummy.next  

if __name__ == '__main__':
    """
    调换方法见图
    https://leetcode.com/problems/swap-nodes-in-pairs/discuss/11046/My-simple-JAVA-solution-for-share
    注意这里必须要不仅要记录当下两个node, 还要前一个node, 因为前一个node也有指针..
    理解这个调换: pre a b的值不变! 我们只需要改指针. 
    pre.next 和 b.next实际上是外面的接口, 需要早赋值. 其他的内部就直接赋值好了. 
    """
    def singleListInit(l):
        if len(l) == 0:
            return None
        else:
            cur = ListNode(l[0])
            cur.next = singleListInit(l[1:])
            return cur
    head = singleListInit([1,2,3,4,5,6,7,8,9])
    # print(head)
    s = Solution()
    print(s.swapPairs(head))
    # print(s.swapTriple(head))
    
