#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
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
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """    
        if n <= 1 or n - m == 0:  # m和n不相同
            return head
        dummy = ListNode(None)
        dummy.next = head
        a = dummy
        for _ in xrange(m - 1):
            a = a.next
        c = a.next  # 只需要初始化这一个
        for _ in xrange(n - m):  # 先赋值, 再给next赋值
            b = a.next
            d = c.next
            e = d.next
            a.next = d
            d.next = b
            c.next = e
        return dummy.next  # Note 不是return head!!""

    # def reverseBetween(self, head, m, n):
    #     # 去掉元素e, 再去掉元素d, 即维护abc.
    #     dummy = ListNode(None)
    #     dummy.next = head
    #     a = dummy
    #     for _ in xrange(m - 1):
    #         a = a.next
    #     b = a.next  # 这样写也不需要最前面的判断了. 
    #     c = b
    #     for _ in xrange(n - m):
    #         a.next = c.next
    #         c.next = c.next.next
    #         a.next.next = b
    #         b = a.next
    #     return dummy.next  # Note 不是return head!!

    # def reverseBetween(self, head, m, n):
    #     # 维护acd. 更快一些.
    #     dummy = ListNode(None)
    #     dummy.next = head
    #     a = dummy  # the node before first reverse node
    #     for _ in range(m - 1):
    #         a = a.next
    #     c = a.next
    #     d = c.next
    #     for _ in range(n - m):
    #         c.next = d.next
    #         d.next = a.next
    #         a.next = d
    #         d = c.next  # 忘掉这一句了...
    #     return dummy.next    

if __name__ == '__main__':
    """
    题设; 把m到n个翻转过来
    错解1: 每次把最后一个插到前面来. 但这还是需要额外的for循环找到tail. 
    错解2: 找到lo hi之后交换: 这属于array的算法..
    解法1: 
        每次插入都确保当前部分是完美reverse的, 直到插入n-m次.
        123456
        132456
        143256
        设定与循环有关的abcde元素. 依次赋值即可.
    解法2:
        依次去掉元素e和元素d
        要维护的是reverse之前的那个start 1, 
        和最小值2, 和当前要被插入的最大值high
    解法3:
        维护acd. 其实维护ac也可. 不写了.
    解法3:
        TODO 貌似submission里有更快解法. 内环中尽量少调用next
    """
    s = Solution()
    print(s.reverseBetween(list2Node([1,2,3,4,5]), 1, 2))
    print(s.reverseBetween(list2Node([1,2,3,4,5]), 2, 4))
    print(s.reverseBetween(list2Node([1,2,3,4,5]), 2, 2))
