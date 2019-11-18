#
# @lc app=leetcode id=148 lang=python
#
# [148] Sort List
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
    # def sortList(self, head):
    #     if not head or not head.next:
    #         return head
    
    #     pre, slow, fast = None, head, head
    #     while fast and fast.next:
    #         pre, slow, fast = slow, slow.next, fast.next.next
    #     pre.next = None  # 需要pre的原因是要从slow前面断开. 即从中间断开即可

    #     return self.merge(*map(self.sortList, (head, slow)))[0]
    
    def merge(self, h1, h2):
        cur = dummy = ListNode(None)
        while h1 and h2:
            if h1.val > h2.val:  # 使h1<h2
                h1, h2 = h2, h1
            cur.next = h1
            cur = h1
            h1 = h1.next  # cur.next = None : 不需要断开
        cur.next = h1 or h2
        while cur.next:
            cur = cur.next
        return dummy.next, cur

    def split(self, head, sz): 
        # head是包含在内的起点, 返回的是split后下一段的起点
        pre = None  # 需要至少一个输入
        while sz > 0 and head:
            pre = head
            head = head.next
            sz -= 1
        pre.next = None
        return head  # head可能是None

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        N = 0
        while head:  # 求N
            head = head.next
            N += 1
        
        sz = 1  # 两段中一段的长度
        while sz < N:
            cur = dummy # 每次从头开始循环
            for _ in xrange(0, N - sz, sz * 2):  # i是两段的起点.
                first = cur.next
                second = self.split(first, sz)  # 先断开两个
                third = self.split(second, sz)
                cur.next, tail = self.merge(first, second)  # 和前面脸上 
                tail.next = third  # 和后面连上
                cur = tail  # 是下面两段的前一个值!
            sz *= 2
        return dummy.next

if __name__ == '__main__':
    """
    题设: 常数空间, nlogn
    分析:
        实践中应该存储链表的指针到array, 排序, 再连起来? 
    解法1: 
        bottom-up的merge sort. 我的和答案也不一样.
        https://leetcode.com/problems/sort-list/discuss/166324/c%2B%2B-and-java-legit-solution.-O(nlogn)-time-and-O(1)-space!-No-recursion!-With-detailed-explaination
        流程: 
            先断开两个, 成为单独两段. (第二段至少有一个值)
            再合并两段
            再与前后相接
            用前面的tail作为新的cur
    解法2: 
        递归: 每次slow, fast找到中点
        https://leetcode.com/problems/sort-list/discuss/46710/Clean-python-code
    """
    s = Solution()
    print(s.sortList(list2Node([4,2,3,1])))
    print(s.sortList(list2Node([-1,3,5,0,4])))
