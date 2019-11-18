#
# @lc app=leetcode id=147 lang=python
#
# [147] Insertion Sort List
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
    # def insertionSortList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """        
    #     dummy = ListNode(None)
    #     dummy.next = head
    #     a = dummy  # a 是b前面的一个元素, 需要a因为要拆开b
    #     b = a.next  # b 指向正在被排序的元素
    #     while b:
    #         p = dummy
    #         # 处理bp相等有更快的方式
    #         while p.next.val <= b.val and b is not p.next:
    #             p = p.next
    #         if b is not p.next:
    #             p2 = p.next
    #             a.next = b.next
    #             p.next = b
    #             b.next = p2
    #             b = a.next
    #         else:
    #             a = a.next
    #             b = a.next
    #     return dummy.next
        
    def insertionSortList(self, head):
        dummy = ListNode(None)
        dummy.next = head
        a = dummy  # a 是b前面的一个元素, 需要a因为要拆开b
        b = a.next  # b 指向正在被排序的元素
        while b:
            p = dummy
            if a.val <= b.val:  # shortcut
                a = a.next
                b = a.next
                continue
            else:
                while p.next.val <= b.val:
                    p = p.next
                p2 = p.next
                a.next = b.next
                p.next = b
                b.next = p2
                b = a.next
        return dummy.next

if __name__ == '__main__':
    """
    sort stable的意思是同样大小的元素保持了之前的顺序。
    解法1:
        a是b前面的元素, 需要a因为要单独拿出b
        p是搜索的指针, p.next与b比较, 因为需要比较元素前面的元素
        需要处理p和b相同的情况, 做法是循环中check bp是否是同一个元素
    解法2:
        更快的处理pb相同, 直接先看ab相对大小, 
            如果a <= b, 则直接赋值,
            如果a > b, 则一定不会相等.
    """
    s = Solution()
    print(s.insertionSortList(list2Node([4,2,1,3])))
    print(s.insertionSortList(list2Node([-1,3,5,0,4])))
