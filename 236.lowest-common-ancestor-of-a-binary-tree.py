#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): # 实际上是个early stopping.
            return root  # 遇到pq直接返回
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right
      
if __name__ == '__main__':
    """
    题设: 允许返回p或者q本身, p q一定存在 
    分析: 
        难点在于定义返回值. 
        也是一个post order, 先递归再判断
    解法1: 
        首先必须从下往上找，所以先递归再判断。
        返回值四种可能：p q ans， None。
        关键点在于, p和q都只出现了一次. 
        递归时而且 left and right只会出现一次, 这一次赋值root. 
        root上层其他分支都返回None. 
    解法2: 不写了.
        是, 官方解答适用于不存在lca的情况
        答案定义是找到任意一个即返回1. 然后通过全局遍历更新ans...
    """
    s = Solution()
     
# @lc code=end

