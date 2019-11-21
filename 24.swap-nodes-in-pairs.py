#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        next = (',' + self.next.__repr__()) if self.next is not None else ''
        return str(self.val) +  next        

def list2Node(lst):
    dummy = ListNode(0)
    cur = dummy
    for item in lst:
        cur.next = ListNode(item)
        cur = cur.next
    return dummy.next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """        
        dummy = ListNode(None)
        dummy.next = head
        a = dummy
        while a and a.next and a.next.next:
            b = a.next
            c = b.next
            d = c.next
            a.next = c
            b.next = d
            c.next = b
            a = b
        return dummy.next

    # def swapPairs(self, head):
    #     # 省略变量d  
    #     dummy = ListNode(None)
    #     dummy.next = head
    #     a = dummy
    #     while a and a.next and a.next.next:
    #         b = a.next
    #         c = b.next
    #         b.next = c.next       
    #         a.next = c
    #         c.next = b
    #         a = b
    #     return dummy.next

    # def swapPairs(self, head):
    #     # 省略变量c, d  
    #     dummy = ListNode(None)
    #     dummy.next = head
    #     a = dummy
    #     while a and a.next and a.next.next:
    #         b = a.next
    #         a.next = b.next
    #         b.next = b.next.next       
    #         a.next.next = b
    #         a = b
    #     return dummy.next

if __name__ == '__main__':
    """
    题设: 调换每两个元素
    解法1:
        最优雅, 最简单, 直接给相关变量都赋值. 
        这样可以abcd顺序改变next即可... 实在是太简单. 
        当然还是要画图理解. 
    解法2: 去掉变量d
    解法3: 去掉变量c, d
    """
    s = Solution()
    head = list2Node([1,2,3,4,5,6,7,8,9])
    print(s.swapPairs(head))
    # print(s.swapTriple(head))
    
