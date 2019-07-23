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
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     if not head:
    #         return head
    #     pre = None  
    #     while head:
    #         save = head.next
    #         head.next = pre
    #         pre = head
    #         head = save
    #     return pre

    # def reverseList(self, head):
    #     # 我的解法, 太丑了.
    #     def helper(head):
    #         if head.next is None:
    #             return head, head
    #         ret, first = helper(head.next)
    #         ret.next = head
    #         head.next = None
    #         return head, first
    #     if not head:
    #         return None
    #     _, first = helper(head)
    #     return first

    def reverseList(self, head):
        # 我需要return new_head
        def helper(head, new_head):
            if head is None:
                return new_head
            # 原链表的头
            next = head.next  
            # 当前这个head连到了之前的new_head上. 这个head就是new_head了
            head.next = new_head  
            return helper(next, head)            
        return helper(head, None)

if __name__ == '__main__':
    """
    解法1: iterative迭代
    实际上pre是个新的链表, 每次在这个链表前面插入值. 
    所以算法需要的实际就是pre和head这两个链表的start位置. 
    解法2: recursive递归: 
    也是需要两个值, 一个当前的head, 一个新链表的head. 
    """
    s = Solution()
    print(s.reverseList(list2Node([1,2,3,4,5])))

