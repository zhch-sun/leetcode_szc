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
        cur = str(self.val)
        return cur + ', ' + self.next.__repr__() if self.next else cur
        
def list2Node(lst):
    dummy = ListNode(0)
    cur = dummy
    for item in lst:
        cur.next = ListNode(item)
        cur = cur.next
    return dummy.next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """        
        c0 = d0 = ListNode(None)  # cur and dummy
        c1 = d1 = ListNode(None)
        while head:
            if head.val < x:
                c0.next = head
                head = head.next
                c0 = c0.next
                # head.next = None  # 不能在中间加... 有head=None
            else:
                c1.next = head
                head = head.next
                c1 = c1.next
                # head.next = None
        c1.next = None  # Note 易忘!!! 只能在这里加, 防止死循环..
        c0.next = d1.next  # 注意cd
        return d0.next
        
if __name__ == '__main__':
    """
    题设: 坐标小于, 右边大于等于
    解法:
        标准partition的前后找值交换是不可能了. 
        只能分成两组链表.
        注意处理最后的尾巴!!!!!
    """
    s = Solution()
    print(s.partition(list2Node([1,4,3,2,5,2]), 3))

