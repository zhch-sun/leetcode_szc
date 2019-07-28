#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    # def connect(self, root):
    #     """
    #     :type root: Node
    #     :rtype: Node
    #     """
    #     save = root
    #     while root and root.left:  # root是为了corner case; root.left是正常结束
    #         cur = root
    #         pre = None
    #         while cur:
    #             if pre is not None:
    #                 pre.right.next = cur.left
    #             cur.left.next = cur.right
    #             pre = cur
    #             cur = cur.next
    #         root = root.left  # the most left pos
    #     return save

    def connect(self, root):
        save = root
        while root and root.left:  # root是为了corner case; root.left是正常结束
            cur = root
            while cur:
                cur.left.next = cur.right
                cur.right.next = cur.next.left if cur.next is not None else None
                cur = cur.next
            root = root.left  # the most left pos
        return save   

if __name__ == '__main__':
    """
    其实就是两个循环, 外环从上到下, 内环从左到右. 
    重要的是内环因为前面已经连好了next, 所以可以用next方便得从左向右iter
    答案1: 第一遍写还是没有注意结束条件.. 不能while root..
    答案2: 甚至不需要pre.. 直接靠着新生成的next就能访问下一个位置. 
    另外答案还有这种写法: root.right.next = root.next and root.next.left可读性太差了.
    """
    s = Solution()

