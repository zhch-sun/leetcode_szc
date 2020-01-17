#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
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
    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """            
    #     cur = dummy = ListNode(None)
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #             cur = cur.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #             cur = cur.next
    #     cur.next = l1 or l2
    #     return dummy.next

    def mergeTwoLists(self, l1, l2):  
        cur = dummy = ListNode(None)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1  # 很聪明
            cur.next = l1
            l1 = l1.next 
            cur = cur.next
        cur.next = l2
        
        return dummy.next       

    # def mergeTwoLists(self, l1, l2):
    #     if l1 and l2:
    #         if l1.val > l2.val:
    #             l1, l2 = l2, l1
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #     return l1 or l2

if __name__ == '__main__':
    """
    解法1:
        正常的赋值
    解法2:
        聪明的swap可以减少代码量. 减少错误
    解法3:
        递归写法
    """
    s = Solution()
    l1 = list2Node([1,2])
    l2 = list2Node([1,3])    
    print(s.mergeTwoLists(l1, l2))
