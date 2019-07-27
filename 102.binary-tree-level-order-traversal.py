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
    #     # 这个就是BFS的解法. 
    #     if not root:
    #         return []
    #     res = []
    #     level = [root]  # hold tree node in a level
    #     while level:
    #         res.append([node.val for node in level])
    #         # 如果不用list comprehension需要新增一个level_new再赋值..
    #         # 但即使用list comprehension这里也是需要两份的内存
    #         level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
    #     return res
    
    # def levelOrder(self, root):
    #     # listcomprehension的内存占用是上下两侧node之和. 
    #     # 这里用可以在前面删除的deque可以在循环中把上层node pop出来
    #     # deque接口: append() appendleft(), pop(), popleft()
    #     # 依旧是bfs
    #     if not root:
    #         return []
    #     res = []
    #     level = deque([root])
    #     while level:
    #         res.append([node.val for node in level])
    #         size = len(level)
    #         for _ in range(size):
    #             cur = level.popleft()
    #             if cur.left is not None:
    #                 level.append(cur.left)
    #             if cur.right is not None:
    #                 level.append(cur.right)
    #     return res

    def levelOrder(self, root):
        # DFS也是正确的, 需要记录level数. 
        # DFS也可以方便进行pre-order post-order traversal?
        res = []
        level = 0
        self.level_helper(root, 0, res)
        return res
    
    def level_helper(self, root, height, res):
        if not root:
            return
        if height == len(res):
            res.append([])
        res[height].append(root.val)
        self.level_helper(root.left, height + 1, res)
        self.level_helper(root.right, height + 1, res)


if __name__ == '__main__':
    """
    BFS和DFS分别在不同情况下可以节省内存. BFS适合与瘦高(lean), DFS适合于胖的.
    DFS的内存是call stack: 所有的recursion必须要靠call stack的占用. 
    BFS的内存是个queue.
    https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33468/One-of-C%2B%2B-solutions-(preorder)
    """
    s = Solution()


