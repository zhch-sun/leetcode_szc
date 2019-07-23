#
# @lc app=leetcode id=147 lang=python
#
# [147] Insertion Sort List
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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 95%
        pre = dummy = ListNode(None)  #用pre代表之前的插入位置。 
        cur = dummy.next = head
        while cur and cur.next:  #  and cur.next
            val = cur.next.val  # 必须用cur.next的值，因为我们需要被插入数据的前面的node
            if cur.val < val:
                cur = cur.next # 必须要有这里才对，确保pre.next不会是cur.next自己
                continue
            if pre.next.val > val:
                pre = dummy
            while pre.next.val < val:  # 去掉 while pre.next 加速了10%..
                pre = pre.next
            # 此时 pre <= cur.next < pre.next。 
            new = cur.next
            cur.next = new.next  # 因为被跳过的元素已经有指针了。
            new.next = pre.next
            pre.next = new  # 为什么人家就能写对？

        return dummy.next
        

if __name__ == '__main__':
    """
    sort stable的意思是同样大小的元素保持了之前的顺序。
    TODO 到底要怎样一次写出正确的插入呀。。但是这道题本身貌似不会考？
    """
    s = Solution()
    print(s.insertionSortList(list2Node([4,2,1,3])))
    print(s.insertionSortList(list2Node([-1,0,3,4,5])))
