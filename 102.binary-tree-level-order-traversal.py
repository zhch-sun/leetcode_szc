#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    # def levelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """        
    #     if not root:
    #         return []
    #     ans = []
    #     level = [root]  # 总是忘记里面的root...
    #     while level:
    #         ans.append([x.val for x in level])  # 忘记x.val
    #         # 不用list compre的话需要tmp存储内部变量. 
    #         level = [x for node in level for x in (node.left, node.right) if x]
    #     return ans

    def levelOrder(self, root):
        if not root:
            return []
        res = []
        level = deque([root])
        while level:
            res.append([node.val for node in level])
            size = len(level)
            for _ in range(size):
                cur = level.popleft()
                if cur.left is not None:
                    level.append(cur.left)
                if cur.right is not None:
                    level.append(cur.right)
        return res

    # def levelOrder(self, root):
    #     if not root:
    #         return []
    #     dq = deque([root])  # 循环中dq里面不是None
    #     ans = []
    #     while dq:
    #         ans.append([x.val for x in dq])  # 先赋值...
    #         for _ in xrange(len(dq)):
    #             cur = dq.popleft()  # 是popleft... 不是pop右边!
    #             if cur.left:
    #                 dq.append(cur.left)
    #             if cur.right:
    #                 dq.append(cur.right)
    #     return ans

    # def levelOrder(self, root):
    #     # DFS也是正确的, 需要记录level数. 
    #     # DFS也可以方便进行pre-order post-order traversal?
    #     def helper(root, height, res):
    #         if not root:
    #             return
    #         if height == len(res):  # 这里还要动态加入[]
    #             res.append([])
    #         res[height].append(root.val)  # 先搞自己. 再左右
    #         helper(root.left, height + 1, res)
    #         helper(root.right, height + 1, res)        
    #     res = []
    #     helper(root, 0, res)
    #     return res

if __name__ == '__main__':
    """
    分析: 
        BFS和DFS分别在不同情况下可以节省内存. BFS适合与瘦高(lean), DFS适合于胖的.
        DFS的内存是call stack: 所有的recursion必须要靠call stack的占用. 
        BFS的内存是个queue.
        https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33468/One-of-C%2B%2B-solutions-(preorder)
    解法1: 
        BFS迭代, 标准解法
        使用deque记录某一层的所有值, 
        循环中需要预先把val都存起来, 然后再用一个循环popleft! 不能pop
    解法2: 
        BFS迭代, list comprehension
        不用deque, 直接用[]存level
        相比解法1会多用一些内存. 用上下两层node的内存. 解法1是一层的内存.
    解法3: 
        DFS需要记录层数
        """
    s = Solution()

