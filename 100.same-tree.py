#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)
        # return p is q  # check if all None
        return True if p is None and q is None else False

