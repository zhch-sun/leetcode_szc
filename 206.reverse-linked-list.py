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
    #         if (not head) or (not head.next):
    #             return head, head
    #         ret, first = helper(head.next)
    #         ret.next = head
    #         head.next = None
    #         return head, first
    #     if not head:
    #         return None
    #     _, first = helper(head)
    #     return first

    # def reverseList(self, head):
    #     if (not head) or (not head.next):
    #         return head
    #     node = self.reverseList(head.next)
    #     head.next.next = head  # 这个是因为，123 54. head指向的是4.next, 然后赋值
    #     head.next = None  # 很容易忘记。
    #     return node

    def reverseList(self, head):
        # 我需要return new_head
        def helper(head, new_head):
            # 尾递归模式。每次把head从head中剥离，然后把head放在new_Head的前面
            if head is None:
                return new_head
            # 原链表的下一个点
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
    我的解法：也是需要两个值, 一个当前的head, 一个新链表的head. 
    答案1：不需要两个值，直接返回新联邦的head就可以。但是我们每次是要再新链表的tail加值呀，
        这里用了个trick， 当前的head的next就是tail！
    答案2：尾递归模式
    """
    s = Solution()
    print(s.reverseList(list2Node([1,2,3,4,5])))

