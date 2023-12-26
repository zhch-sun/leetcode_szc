#
# @lc app=leetcode id=222 lang=python
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def countNodes(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     return 0 if not root else 1 + self.countNodes(root.left)\
    #          + self.countNodes(root.right)

    def countNodes(self, root):
        def leftHeight(root):
            h = 0
            while root:
                root = root.left
                h += 1
            return h
        if not root:
            return 0
        hl = leftHeight(root.left)
        hr = leftHeight(root.right)
        if hl == hr: 
            return (1 << hl) + self.countNodes(root.right)  # Note括号..
        else:
            return (1 << hr) + self.countNodes(root.left)

if __name__ == '__main__':
    """
    解法1: 不考虑complete的性质
    解法2: o(h^2), 
        check的是左右子节点的最左边!. 注意两个子树都是向左递归!
        注意个数是root + left子树 1 + ((1 << hl) - 1)
        忘记括号了!
    """
    s = Solution()
    
# @lc code=end

