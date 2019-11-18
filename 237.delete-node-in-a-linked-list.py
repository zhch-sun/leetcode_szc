#
# @lc app=leetcode id=237 lang=python
#
# [237] Delete Node in a Linked List
#

# @lc code=start
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
    # def deleteNode(self, node):
    #     """
    #     :type node: ListNode
    #     :rtype: void Do not return anything, modify node in-place instead.
    #     """
    #     a = node
    #     b = node.next

    #     while b.next:
    #         a.val = b.val
    #         a, b = a.next, b.next  # 还是写错了. 
    #     a.val = b.val
    #     a.next = None
        
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    """
    题设: 给定一个非末尾结点, 删除该结点
    解法1: 
        不停copy. 还是需要画图并给两个位置赋值.
    解法2:
        只copy一个值.. 然后跳过下一个结点...
    """
    s = Solution()
    # print(s.deleteNode(list2Node([4,5,1,9]), 5))
# @lc code=end

