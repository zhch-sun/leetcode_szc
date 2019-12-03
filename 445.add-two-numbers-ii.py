#
# @lc app=leetcode id=445 lang=python
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val) + (', ' + self.next.__repr__() \
            if self.next else '')

class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     def count(p):
    #         n = 0
    #         while p:
    #             p = p.next
    #             n += 1
    #         return n
        
    #     def dfs(l1, l2, offset):
    #         if not l1 and not l2:
    #             return None, 0
    #         if offset > 0:
    #             node, carry = dfs(l1, l2.next, offset - 1)
    #             carry, val = divmod(l2.val + carry, 10)
    #         else:
    #             node, carry = dfs(l1.next \
    #                 if l1 else None, l2.next if l2 else None, 0)
    #             carry, val = divmod((l1.val if l1 else 0) + l2.val + carry, 10)
    #         cur = ListNode(val)
    #         cur.next = node
    #         return cur, carry
        
    #     n1 = count(l1)
    #     n2 = count(l2)
    #     if n1 > n2:  # 确保l1 <= l2
    #         l1, l2 = l2, l1
    #         n1, n2 = n2, n1  #忘了这个..

    #     cur, carry = dfs(l1, l2, n2 - n1)
    #     if carry:  # carry不可能大于9
    #         node = ListNode(carry)
    #         node.next = cur
    #         return node
    #     return cur

    def addTwoNumbers(self, l1, l2):
        a1 = []
        while l1:
            a1.append(l1.val)
            l1 = l1.next
        a2 = []
        while l2:
            a2.append(l2.val)
            l2 = l2.next
        carry = 0
        dummy = ListNode(None)
        while a1 or a2 or carry:
            c1 = a1.pop() if a1 else 0
            c2 = a2.pop() if a2 else 0
            carry, val = divmod(c1 + c2 + carry, 10)
            node = ListNode(val)
            node.next = dummy.next
            dummy.next = node
        return dummy.next

if __name__ == '__main__':
    """
    题设: 正序输入, 不允许翻转链表. 
    坑:
        一个0, 0+0, 自动是对的..
    解法1:
        我的解法. 
        计算链表长度, 然后dfs中隐式补齐链表.
    解法2:
        直接把两个链表放到array/stack里面加...
    解法3: 没写.
        或者直接把两个链表转化成int... python int无限大..
    """
    s = Solution()
    def list2node(l):
        cur = dummy = ListNode(0)
        for item in l:
            cur.next = ListNode(item)
            cur = cur.next
        return dummy.next

    s = Solution()
    print(s.addTwoNumbers(list2node([7,2,4,3]), list2node([5,6,4])))        
# @lc code=end

