#
# @lc app=leetcode id=124 lang=python
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, root.val + left + right)
            # Note +val 的位置!! 非常容易错...
            return max(0, root.val + left, root.val + right)  

        self.ans = float('-inf')  # 必须加self.
        dfs(root)
        return self.ans
        
if __name__ == '__main__':
    """
    题设: 类似543, 树的直径. 只不过有了权值.
    解法:
        类似max subarray, 加左边, 加右边, 不加. 
        注意有不加的可能性
    """
    s = Solution()
    
# @lc code=end

