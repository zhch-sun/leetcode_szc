#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        n = 1
        cur = head
        # 不能while cur, 因为我们还需要最后一个node的指针.
        while cur.next is not None:
            n += 1
            cur = cur.next
        tail = cur
        tail.next = head  #必须要在这里cycle起来, 否则1个输入的时候会有bug，也方便后面的逻辑

        # cur = tail  #从head移需要n-=(k+1), 或者从tail开始移.
        k = k % n
        n -= k
        while n:
            tail = tail.next
            n -= 1
        
        head = tail.next
        tail.next = None
        return head


if __name__ == '__main__':
    """
    注意要在中间先把尾巴和头连起来... 用来解决1个input时候的问题.
    slow fast貌似并没有变快? 还不如count
    TODO slow fast
    """
    s = Solution()
    # print(s.rotateRight())
        

