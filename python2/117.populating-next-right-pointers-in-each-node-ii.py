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
    #     from collections import deque
    #     if not root:
    #         return None
    #     dq = deque([root])
    #     while dq:
    #         pre = None
    #         for _ in xrange(len(dq)):
    #             cur = dq.popleft()
    #             if cur.left:
    #                 dq.append(cur.left)
    #             if cur.right:
    #                 dq.append(cur.right)
    #             if pre:
    #                 pre.next = cur
    #             pre = cur
    #     return root

    # def connect(self, root):
    #     if not root:
    #         return None
    #     save = root
    #     while root:  # root是最左边节点
    #         cur = root
    #         root = None  # 不知道下一层是否有root
    #         pre = None  # 内环前更新变量
    #         while cur:
    #             if cur.left:
    #                 if pre:
    #                     pre.next = cur.left
    #                 else:
    #                     root = cur.left  # Note 更新最左边节点
    #                 pre = cur.left
    #             if cur.right:
    #                 if pre:
    #                     pre.next = cur.right
    #                 else:
    #                     root = cur.right
    #                 pre = cur.right
    #             cur = cur.next
    #     return save

    def connect(self, root):
        dummy = Node(None, None, None, None)
        dummy.next = root
        while dummy.next:  # root是最左边节点
            cur = dummy.next  # 循环内部dummy会自动更新到下一层...
            dummy.next = None  # 又忘记了..
            pre = dummy
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = cur.left
                if cur.right:
                    pre.next = cur.right
                    pre = cur.right
                cur = cur.next
        return root

if __name__ == '__main__':
    """
    题设: 要求O(1)空间.
    解法1:
        通解: 使用level遍历. 同116. 但是用了额外空间.
    解法2:
        相比于116, next指针可能要隔山打牛, 所以需要存pre
        不仅要存pre, 每行第一个head值不是上一个行首的left!!!
        所以循环中还要更新root, 注意内环开始前要把root赋值为None..
    解法2: 用dummy head替换掉原来的真head, 节省逻辑.
        dummy处理行首不存在的情况.
        dummy内环前也要None...
        另外如果循环中用root来做, 逻辑更简单. 
    """
    s = Solution()
