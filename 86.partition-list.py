#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        next = ',' + self.next.__repr__() if self.next else ''
        return str(self.val) + next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy0 = ListNode(None)
        dummy1 = ListNode(None)
        head0 = dummy0
        head1 = dummy1
        while head is not None:
            if head.val < x:
                # head0 = head0.next = head  # 写成一行有bug!!!
                head0.next = head
                head0 = head0.next
            else:
                # head1 = head1.next = head
                head1.next = head
                head1 = head1.next
            head = head.next
        head1.next = None  # Note 这个很容易忘!
        head0.next = dummy1.next
        return dummy0.next

        
if __name__ == '__main__':
    """
    分成两组链表.
    注意处理最后的尾巴!!! 需要赋值None
    """
    s = Solution()
    def list2Node(input):
        dummy = ListNode(0)
        cur = dummy
        for item in input:
            cur.next = ListNode(item)
            cur = cur.next
        return dummy.next
    print(s.partition(list2Node([1,4,3,2,5,2]), 3))

