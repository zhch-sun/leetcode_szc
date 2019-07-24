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
        # if not root:
        #     return True
        return self.helper(root) != -1

    def helper(self, root):
        if not root:
            return 0  # height for None!
        left = self.helper(root.left)
        # if left == -1:  # put it here to break early, why not faster?
        #     return -1
        right = self.helper(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
        

if __name__ == '__main__':
    """
    定义是每一个节点的两个子树的高度差小于1
    这题并不能通过最大和最小高度来判断:
        比如1左边是2, 2左边是三, height都是3, 但是不平衡: 
        因为height是指从某个node出发的最大高度!
    答案是通过dfs过程中返回高度来实现的.
    无法直接跳出recursion. 如果想跳出, 只能搞try Exception了...
    TODO: 要写iterative的post-order traversal吗?
    """
    s = Solution()
        

