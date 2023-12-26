#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        dummy = ListNode(None)
        dummy.next = head
        c = head  # cur 
        # dummy和c是循环不变量
        while c and c.next:  # 需要c处理空输入的情况
            b = dummy.next
            d = c.next  # d是正在被插入的元素
            e = d.next
            dummy.next = d
            d.next = b
            c.next = e
        return dummy.next

    # def reverseList(self, head):
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
    #     if (not head) or (not head.next):
    #         return head
    #     node = self.reverseList(head.next)
    #     head.next.next = head  # 这个是因为，123 54. head指向的是4.next, 然后赋值
    #     head.next = None  # 很容易忘记。
    #     return node

    # def reverseList(self, head):
    #     # 我需要return new_head
    #     def helper(head, new_head):
    #         # 尾递归模式。每次把head从head中剥离，然后把head放在new_Head的前面
    #         if head is None:
    #             return new_head
    #         # 原链表的下一个点
    #         next = head.next  
    #         # 当前这个head连到了之前的new_head上. 这个head就是new_head了
    #         head.next = new_head  
    #         return helper(next, head)            
    #     return helper(head, None)

if __name__ == '__main__':
    """
    解法1: 迭代
        循环第i次时候, 保证前i个数是reverse的. 
        这样只要每次在前面插入值即可. 
        12345
        对应dummy b c d e. d是被插入的数.
    解法2: 迭代优化.
    解法2: 递归: 
        直接返回新链表的head就可以。
        但是我们每次是要再新链表的tail加值呀，
        这里用了个trick， 当前的head的next就是tail！
    答案2：尾递归模式
    """
    s = Solution()
    print(s.reverseList(list2Node([1,2,3,4,5])))

