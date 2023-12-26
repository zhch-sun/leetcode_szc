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
        if not head:  # 会有[]的test case?? input不是应该是 ListNode嘛..
            return head        
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

if __name__ == '__main__':
    """
    
    """
    s = Solution()
    # print(init_list([1,1,2,3,3]))
    print(s.deleteDuplicates(list2Node([1,1,2])))
    print(s.deleteDuplicates(list2Node([1,1,2,3,3])))

