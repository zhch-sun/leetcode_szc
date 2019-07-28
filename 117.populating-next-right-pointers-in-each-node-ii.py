#
# @lc app=leetcode id=117 lang=python
#
# [117] Populating Next Right Pointers in Each Node II
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
    #     # while root and root.left: # 这里也错了. 
    #     while root:
    #         cur = root
    #         pre = None
    #         head = None
    #         while cur:
    #             if cur.left:
    #                 if pre:
    #                     pre.next = cur.left
    #                 else:
    #                     head = cur.left
    #                 pre = cur.left
    #             if cur.right:
    #                 if pre:
    #                     pre.next = cur.right
    #                 else:
    #                     head = cur.right
    #                 pre = cur.right
    #             cur = cur.next
    #         # root = root.left  # 原来是这里错了... 不能保证left一定有值..
    #         root = head
    #     return save

    def connect(self, root):
        dummy = Node(0, None, None, None)  # dummy head
        dummy.next = root
        while dummy.next:
            cur = dummy.next
            dummy.next = None  # new head
            pre = dummy
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = cur.left
                if cur.right:
                    pre.next = cur.right
                    pre = cur.right
                cur = cur.next  # 忘了这个!!
        return root

if __name__ == '__main__':
    """
    解法1: 第一遍写出了错解, 
        错误1: 不能够保证root.left是下一层开始的位置.
        错误2: 最外层不能是root and root.left, left不一定存在了...
    解法2: 用dummy head替换掉原来的真head, 节省逻辑.
        理解什么时候需要dummy!
        另外如果循环中用root来做, 逻辑更简单. 
    解法3: 用一个while loop.. 但是我觉得影响可读性? 而且实际速度也不快, 不写.
    """
    s = Solution()
