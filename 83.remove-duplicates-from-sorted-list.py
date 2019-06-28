#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        next = ', ' + self.next.__repr__() if self.next is not None else ''
        return str(self.val) + next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:  # 为什么会有[]的test case?? input不是应该是 ListNode嘛..
            return head
        cur = head
        while cur.next is not None:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == '__main__':
    """
    
    """
    s = Solution()
    def init_list(l):
        cur = root = ListNode(None)
        for i in l:
            cur.next = ListNode(i)
            cur = cur.next
        return root.next
    
    # print(init_list([1,1,2,3,3]))
    print(s.deleteDuplicates(init_list([1,1,2,3,3])))

