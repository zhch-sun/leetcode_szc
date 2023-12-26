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
    #     from collections import deque             
    #     if not root:
    #         return None
    #     dq = deque([root])
    #     while dq:
    #         pre = Nxone  # Note 每个循环开头更新
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

    def connect(self, root):
        save = root
        while root and root.left:  # 注意条件, 是有子节点. 两个都要判断..
            cur = root
            while cur:  
                cur.left.next = cur.right  # Note 不是cur.right.next..
                cur.right.next = cur.next.left if cur.next else None  # Note
                cur = cur.next
            root = root.left
        return save

if __name__ == '__main__':
    """
    解法1:
        题设要求O(1)空间...
        通用解法: 不要求perfect. 
        层序遍历, 注意每个循环开头pre=None
    解法2:
        因为perfect, 所以left右边一定紧连right, 所以可以两个方向遍历.
        内环可以直接用next遍历.
        坑:
            主循环既要保证下面有值, 又要保证root不为空
            不要忘记right要赋值给另外一边的left..
    """
    s = Solution()

