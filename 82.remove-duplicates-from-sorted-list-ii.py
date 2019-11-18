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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        dummy = ListNode(None)
        dummy.next = head
        a = dummy
        while a.next is not None:
            b = a.next
            if b.next and b.next.val == b.val:
                while b.next and b.next.val == b.val:
                    b = b.next  # b停留的地方也要删除
                a.next = b.next  # Note 后面没有a=a.next!
            else:
                a = a.next
        return dummy.next

if __name__ == '__main__':
    """
    解法1:
        分类讨论. 注意第一个分支没有a=a.next!
    解法2:
        submission有更快解法, 不管了.
    """
    s = Solution()
    print(s.deleteDuplicates(list2Node([1,2,3,3,4,4,5])))
    print(s.deleteDuplicates(list2Node([1,1,1,2,3])))


