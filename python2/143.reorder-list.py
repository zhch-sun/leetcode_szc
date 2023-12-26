#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """        
        if not head or not head.next or not head.next.next:  # 1\2个输入也干掉
            return head
        # 具体写法还是要check n=1,2,3,4,5的情况
        slow = fast = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  # slow是第一部分的最后一个
        # slow相当于直接reverse里面的dummy
        cur = slow.next
        while cur.next:
            d = cur.next
            cur.next = d.next
            d.next = slow.next
            slow.next = d
        
        cur = head
        while slow.next:
            cur2 = slow.next
            slow.next = cur2.next
            cur2.next = cur.next
            cur.next = cur2
            cur = cur.next.next  # 忘记了
        return head

if __name__ == '__main__':
    """
    题设: 把后面半部分的值分拆插入前面半部分
    解法: 
        根据样例以及推理, 奇偶数前面的长度都是 N // 2 + 1
        1找中点, 2reverse后面, 3插入
    """
    s = Solution()
    print(s.reorderList(list2Node([1])))
    print(s.reorderList(list2Node([1,2,3,4,5])))
    print(s.reorderList(list2Node([1,2,3,4,5,6])))
