#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        def helper(root):  # 需要return高度所以需要helper
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return True if helper(root) >= 0 else False  # Note=0亦可!

if __name__ == '__main__':
    """
    分析: 
        定义是所有节点的两个子树的高度差小于1
        这题并不能通过最大和最小高度来判断:
            比如1左边是2, 2左边是三, height都是3, 但是不平衡: 
            因为height是指从某个node出发的最大高度!
        必须通过定义来写. 
    解法:
        需要返回高度, 所以helper
        无法直接跳出recursion. 如果想跳出, 只能搞try Exception了?
    """
    s = Solution()
        