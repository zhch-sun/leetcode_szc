#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None:  # 不需要这个
            # return None
        slow = fast = head
        # fast = slow.next  # 没有这个!!!
        while fast and fast.next:  # Note这个条件
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head  # 重用fast指针.
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


if __name__ == '__main__':
    """
    还是下面定义最清楚:
    https://leetcode.com/problems/linked-list-cycle-ii/discuss/44781/Concise-O(n)-solution-by-using-C%2B%2B-with-Detailed-Alogrithm-Description
    2 * (L1+L2) = L1 + L2 + n * C => L1 = (n - 1) C + (C - L2)*
    根据上述公式, 从head走L1 等于 走C-L2, 
    注意slow和fast正处在L2的位置上, 再走C-L2就是C一整圈, 
    如果此时有个pointer从entry开始走, 那么走L1的路程正好和slow走到起点处相交.

    但是答案中的做法仍然有冗余. 我的答案更简单. 
    """
    s = Solution()

