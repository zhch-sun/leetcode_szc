#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(s, t):
            if s and t:
                return s.val == t.val and isSame(s.left, t.left) \
                    and isSame(s.right, t.right)
            return not s and not t

        if not s:
            return False
        if s.val == t.val and isSame(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

if __name__ == '__main__':
    """
    有用到hash的加速做法
    """
    s = Solution()
    
# @lc code=end

