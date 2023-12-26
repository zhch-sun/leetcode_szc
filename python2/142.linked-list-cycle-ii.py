#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def list2nodeCycle(input, pos=None):
#     # 支持带cycle的链表
#     cur = head = ListNode(0)
#     for i, item in enumerate(input):
#         cur.next = ListNode(item)
#         cur = cur.next
#         if pos is not None and i == pos:
#             cycle = cur        
#     if pos is not None:
#         cur.next = cycle
#     return head.next

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        slow = fast = head  # 不需要空head判断
        while fast and fast.next:  # 其实这里可以用while else语句
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # 这样写最简单
                fast = head  # 重用fast指针.
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

if __name__ == '__main__':
    """
    题设: 需要返回cycle开始的node
    解法:
        https://leetcode.com/problems/linked-list-cycle-ii/discuss/44781/Concise-O(n)-solution-by-using-C%2B%2B-with-Detailed-Alogrithm-Description
        L1是线段, L2是entry到meeting C是cycle总长度
        2 * (L1+L2) = L1 + L2 + n * C ==>> L1 = (n - 1) C + (C - L2)
        根据上述公式, 从head走L1 等于 走C-L2, 
        注意slow和fast正处在L2的位置上, 再走C-L2就是C一整圈, 
        如果此时有个pointer从entry开始走, 那么走L1的路程正好和slow走到起点处相交.
    """
    # s = Solution()
    # l = list2nodeCycle([3,2,0,-4], 1)
    # print(s.detectCycle(l))

