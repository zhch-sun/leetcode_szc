#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        start = dummy  # the node before first reverse node
        for _ in range(m - 1):
            start = start.next
        low = start.next
        high = low.next
        for _ in range(n - m):
            low.next = high.next
            high.next = start.next
            start.next = high
            high = low.next  # 忘掉这一句了...
        return dummy.next
        
if __name__ == '__main__':
    """
    我的思路: 每次把最后一个插到前面来. 但这还是需要额外的for循环找到tail. 
    答案思路: 每次插入都确保当前部分是完美reverse的, 直到插入n-m次. 
    123456
    132456
    143256
    所以要维护的是reverse之前的那个start 1, 和最小值2, 和当前要被插入的最大值high
    """
    s = Solution()
    def list2Node(input):
        dummy = ListNode(0)
        cur = dummy
        for item in input:
            cur.next = ListNode(item)
            cur = cur.next
        return dummy.next
    print(s.reverseBetween(list2Node([1,2,3,4,5]), 1, 2))
    print(s.reverseBetween(list2Node([1,2,3,4,5]), 2, 4))
    print(s.reverseBetween(list2Node([1,2,3,4,5]), 2, 2))

