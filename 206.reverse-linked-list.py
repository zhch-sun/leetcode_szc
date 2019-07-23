#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre = None  
        while head:
            save = head.next
            head.next = pre
            pre = head
            head = save
        return pre
        
if __name__ == '__main__':
    """
    实际上pre是个新的链表, 每次在这个链表前面插入值. 
    所以算法需要的实际就是pre和head这两个链表的start位置. 
    """
    s = Solution()
    print(s.reverseList(list2Node([1,2,3,4,5])))

