#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sym_helper(left, right):
            if left and right:
                return left.val == right.val and \
                    sym_helper(left.left, right.right) and \
                    sym_helper(left.right, right.left)
            else: 
                return left is right
        if not root:
            return True  # None return true
        return sym_helper(root.left, root.right)
        
if __name__ == '__main__':
    """
    
    """
    def t(n):
        return n and (n.val, t(n.left), t(n.right))
    s = Solution()

    # tree = TreeNode(5)
    # tree.left = TreeNode(3)
    # tree.right = TreeNode(3)
    # print(t(tree))
    # print(s.isSymmetric(tree))
