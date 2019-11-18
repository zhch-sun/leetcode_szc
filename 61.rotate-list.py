#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        n = 1
        fast = head
        while fast.next:  # 不能while cur, 因为需要最后一个node的指针.
            n += 1
            fast = fast.next

        k = k % n
        slow = head
        for _ in xrange(n - k - 1):
            slow = slow.next

        fast.next = head  # 必须先连头尾, 再拆中间. 
        head = slow.next
        slow.next = None
        return head

    # def rotateRight(self, head, k):
    #     if not head:
    #         return head
    #     cur = head
    #     N = 0
    #     while cur:  # 这里不能用slow fast, 因为k可能更大. 
    #         cur = cur.next
    #         N += 1
    #     # 这一步需要slow fast, 因为同时需要尾指针和中间.         
    #     k = k % N
    #     slow = fast = head
    #     for _ in xrange(k):
    #         fast = fast.next
    #     while fast.next:  # 判断next最方便, 因为最后要停在尾指针上
    #         fast = fast.next
    #         slow = slow.next
    #     # 接上头尾, 断开中间
    #     fast.next = head  # 必须先接头尾
    #     new_head = slow.next
    #     slow.next = None
    #     return new_head

if __name__ == '__main__':
    """
    题设, rotate链表, k非负. 
    分析: 不会删除第一个元素, 不需要dummy
    解法1:
        第一步需要count个数, 且不能slow fast, 因为k可能大于n
        第二步需要中间指针和尾指针, 如果上面留着尾指针, 这一步直接移动n-k步即可.
        Note需要先把尾巴和头连起来... 用来解决1个input时候的问题.
    解法2:
        如果第一步没有拿到尾指针, 可以slow fast.
        slow fast更快? 
    """
    s = Solution()
    print(s.rotateRight(list2Node([1,2,3,4,5]), 2))
    print(s.rotateRight(list2Node([0,1,2]), 4))
    print(s.rotateRight(list2Node([0]), 4))
        

