#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """        
        slow = fast = head  # 不需判断head是否为空
        while fast and fast.next:  # Note 只判断fast即可
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

def list2nodeCycle(input, pos=None):
    # 支持带cycle的链表
    cur = head = ListNode(0)
    for i, item in enumerate(input):
        cur.next = ListNode(item)
        cur = cur.next
        if pos is not None and i == pos:
            cycle = cur        
    if pos is not None:
        cur.next = cycle
    return head.next

if __name__ == '__main__':
    """
    题设: 返回是否有cycle即可.
    解法:
        快慢指针. 
        证明: 
            可以认为slow是静止, fast的速度是1, 所以一定会追上
            仍要证明不会跳过slow, 一定停在同位置: 
                分类讨论追上的情况, fast不可能跨过slow, 即第一次相遇就可以匹配上. 
    """
    s = Solution()
    l = list2nodeCycle([3,2,0,-4], 1)
    l = list2nodeCycle([1,2], 0)
    l = list2nodeCycle([1,2], None)
    print(s.hasCycle(l))
