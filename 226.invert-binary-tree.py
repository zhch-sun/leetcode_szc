#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     if root:
    #         # left = self.invertTree(root.right)
    #         # right = self.invertTree(root.left)
    #         # root.left = left
    #         # root.right = right
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root
    
    def invertTree(self, root):
        # bfs and dfs
        queue = deque([root])
        while queue:
            # cur = queue.popleft()  # bfs 必须用queue
            cur = queue.pop()  # dfs 这里可以改用list..  
            if cur:
                cur.left, cur.right = cur.right, cur.left
                queue.append(cur.left)
                queue.append(cur.right)
        return root


if __name__ == '__main__':
    """
    解法1: 递归
        不能直接写root.left = self.invertTree(root.right)
        因为这样下面那条语句就不对了... 
        或者写一个python的swap语句, 这个是有cache的...
    解法2: dfs and bfs
    """
    s = Solution()
        

