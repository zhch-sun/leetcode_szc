#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    # def __lt__(self, x):
    #     return self.val < x.val
    
    # def __iter__(self):
    #     cur = self
    #     while cur is not None:
    #         yield cur
    #         cur = cur.next

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

import heapq
class Solution(object):
    # def mergeKLists(self, lists):
    #     # 如果允许自定义iter和lt
    #     cur = dummy = ListNode(None)
    #     for n in heapq.merge(*lists):  # 忘记*了..
    #         cur.next, cur = n, n
    #     return dummy.next

    # def mergeKLists(self, lists):
    #     """
    #     :type lists: List[ListNode]
    #     :rtype: ListNode
    #     """
    #     cur = dummy = ListNode(None)
    #     pq = [(n.val, n) for n in lists if n]
    #     heapq.heapify(pq)  # Note heapify是inplace的..
    #     while pq:
    #         n = heapq.heappop(pq)
    #         nextN = n[1].next
    #         if nextN:
    #             heapq.heappush(pq, (nextN.val, nextN))  #两个input 
    #         cur.next, cur = n[1], n[1]
    #     return dummy.next

    def mergeKLists(self, lists):
        def merge(l1, l2):
            cur = dummy = ListNode(None)
            while l1 and l2:
                if l1.val > l2.val:
                    l1, l2, = l2, l1
                cur.next = l1
                cur = l1
                l1 = l1.next
            cur.next = l1 or l2
            return dummy.next
        sz = 1
        k = len(lists)
        while sz < k:
            for i in xrange(0, k - sz, sz * 2):
                lists[i] = merge(lists[i], lists[i + sz])  # Note
            sz *= 2
        return lists[0] if lists else None

if __name__ == '__main__':
    """
    分析: 
        merge题有两种思路, 
            1. heapq
            2. merge sort
    解法1: 
        希望直接用merge, 需要把listnode变成个可以iter的
        heapq merge的generator里面, 返回的是数.. 
            所以需要直接比较iter.. 
            因此还要定义__lt__
        注意merge的输入是*lists!!!. 忘记*
        而且merge也不能加key或者cmp
    解法2:
        用heapq, 不改数据结构. 队列里面的东西只能是(x.val, x)...
        类似378题, 只有行有序, 手动merge
        设链表总长度为N, 则复杂度为NlogK, 空间是O(k)
    解法3:
        两两合并, 复杂度kN. 空间O(1)
    解法4:
        类似于bottom-up merge的分治! 好聪明.. 复杂度NlogK, 空间O(1)
        注意:
            合并时, 不改变array大小!
            还是利用index去索引, 返回值直接存在i上.
    """
    s = Solution()
    print(s.mergeKLists([list2Node([1,4,5]), \
        list2Node([1,3,4]), list2Node([2,6])]))
        

