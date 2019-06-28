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

if __name__ == '__main__':
    """
    注意python 答案中的 tupleify 做法中的 and的使用:
    https://stackoverflow.com/questions/47007680/strange-use-of-and-or-operator
    and: Return the first Falsy value if there are any, else return the last value in the expression.
    """ 
    s = Solution()
    
    def t(n):
        # return n and (n.val, t(n.left), t(n.right))
        return n and (n.val, t(n.left), t(n.right))
    
    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.right = TreeNode(2)

    print(t(tree))
