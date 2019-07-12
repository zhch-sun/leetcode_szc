#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def removeNthFromEnd(self, head, n):
    #     """
    #     :type head: ListNode
    #     :type n: int
    #     :rtype: ListNode
    #     """
    #     # 97%
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     slow = fast = dummy
    #     for _ in xrange(n + 1):
    #         fast = fast.next

    #     while fast is not None:
    #         fast = fast.next
    #         slow = slow.next

    #     slow.next = slow.next.next
    #     return dummy.next

    def removeNthFromEnd(self, head, n):
        def remove(head):
            if head is None:
                return 0, head
            i, head.next = remove(head.next)
            return i + 1, [head, head.next][i + 1 == n]
        return remove(head)[1]

    
if __name__ == '__main__':
    """
    一种最靠谱做法, 维护两个指针，中间差距为n
    需要dummy node来解决只有一个node并删掉的情况. (也可以不用dummy...)
    这个题从后到前明显可以stack或者recursive. 但这实际上就是把node push到list里...
    """
    s = Solution()
    
