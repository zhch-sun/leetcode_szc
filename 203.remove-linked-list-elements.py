#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#
def list2Node(input):
    dummy = ListNode(0)
    cur = dummy
    for item in input:
        cur.next = ListNode(item)
        cur = cur.next
    return dummy.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        next = ',' + self.next.__repr__() if self.next else ''
        return str(self.val) + next        

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = dummy = ListNode(None)
        dummy.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next  #Note 这里后面不能再跟cur=cur.next了...
            else:
                cur = cur.next
                
        return dummy.next

if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.removeElements(list2Node([1,2,6,3,4,5,6]), 6))   

