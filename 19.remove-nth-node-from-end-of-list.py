#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 97%
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        for _ in xrange(n + 1):  # for比while好
            fast = fast.next  # 此时fast可能是None
        while fast is not None:  # 一般都check fast而不是fast.next
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

    # def removeNthFromEnd(self, head, n):
    #     def remove(head):
    #         if head is None:
    #             return 0, head
    #         i, head.next = remove(head.next)
    #         return i + 1, [head, head.next][i + 1 == n]
    #     return remove(head)[1]
    
if __name__ == '__main__':
    """
    题设: 
        去掉倒数第n个元素, 最终返回head.
    解法1:
        slow fast指针. 
    解法2:
        第一遍算出个数. 第二遍找到N-n的位置. 
        其实复杂度一样, 但是第一种可能cache friendly? 

    """
    s = Solution()
    print(s.removeNthFromEnd(list2Node([1,2,3,4,5]), 2))
    print(s.removeNthFromEnd(list2Node([1]), 1))
    
