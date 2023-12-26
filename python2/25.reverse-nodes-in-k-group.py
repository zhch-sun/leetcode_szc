#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(a, k):
            c = a.next
            for i in xrange(k - 1):
                if c.next is None:
                    return reverse(a, i + 1)  # Note i + 1
                b = a.next
                d = c.next
                e = d.next
                a.next = d
                d.next = b
                c.next = e
            return c  # 返回的是最后的值!
        dummy = ListNode(None)
        dummy.next = head
        a = dummy
        while a.next is not None:  # 必须是a.next.. 
            a = reverse(a, k)  # a是上一个迭代的c
        return dummy.next

if __name__ == '__main__':
    """
    题设: k的取值有意义
        24题follow up, 92题followup, 依旧abcde
    处理最后一部分的方式:
        1. 先计算总长度. 然后N//k即可, 这还要o(N)的时间
        2. 如果遇到最后有首位的k, 把后面再反转回来. 见下面cpp的答案
        https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11457/20-line-iterative-C%2B%2B-solution
    解法1:
        注意外环是a.next 是None
        corner case时, 是i + 1!.
    解法2:
        参加submission里最快饿解法. 
        内环非常简单. 
    """
    s = Solution()
    print(s.reverseKGroup(list2Node([1,2,3,4,5]), 2))
    print(s.reverseKGroup(list2Node([1,2,3,4,5]), 3))
# @lc code=end

