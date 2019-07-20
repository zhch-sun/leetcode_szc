#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head and head.next:
            if pre.next.val == head.next.val:
                while head.next and pre.next.val == head.next.val:
                    head = head.next
                pre.next = head.next
                head = head.next
            else:
                pre = head
                head = head.next
        return dummy.next
        
if __name__ == '__main__':
    """
    突然理解了, 之所以需要dummy, 是因为我们需要一个node, 它的指针指向第一个node. 
    只能是两个while了...没有更好的解法了.
    而且还需要分类讨论
    """
    s = Solution()
    def list2Node(input):
        dummy = ListNode(0)
        cur = dummy
        for item in input:
            cur.next = ListNode(item)
            cur = cur.next
        return dummy.next
    print(s.deleteDuplicates(list2Node([1,2,3,3,4,4,5])))
    print(s.deleteDuplicates(list2Node([1,1,1,2,3])))


