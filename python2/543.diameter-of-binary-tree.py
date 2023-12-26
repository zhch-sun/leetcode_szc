#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        self.ans = 0
        dfs(root)
        return self.ans
        
if __name__ == '__main__':
    """
    题设: 是所有点之间的最长路径, 不必通过最高点. 计算edge的数目.
    解法:
        枚举所有最高点. 分别求每个最高点的最大值. 
        注意长度是edge的个数不是node的个数.
        需要两种值,
            一个是左右子树最大的单向长度, 一个是两边加起来的长度.
            也可以不用全局变量, 两种值都return
    """
    s = Solution()
    
# @lc code=end

