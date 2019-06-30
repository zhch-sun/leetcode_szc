#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        walker = head
        runner = head  # Note not head.next!!!
        # Note 1. the logic is and!!! 2. not just walker and runner
        # Note is not walker.next, its runner.next....
        while runner is not None and runner.next is not None:
            walker = walker.next
            runner = runner.next.next
            if walker == runner:
                return True
        return False

def list2node(input, pos=None):
    cur = head = ListNode(0)
    for i, item in enumerate(input):
        cur.next = ListNode(item)
        cur = cur.next
        if pos is not None and i == pos:
            cycle = cur        
    if pos is not None:
        cur.next = cycle
    return head.next

if __name__ == '__main__':
    """
    具体实现还是很tricky的..
    用mod来做数学推倒. 
    """
    s = Solution()
    l = list2node([3,2,0,-4], 1)
    l = list2node([1])
    print(s.hasCycle(l))
