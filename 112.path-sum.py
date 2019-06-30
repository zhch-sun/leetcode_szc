#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def hasPathSum(self, root, sum):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: bool
    #     """
    #     if not root:
    #         return False
    #     sum -= root.val
    #     # if sum < 0:  # can not use this because of negative number
    #     #     return False
    #     if root.left is None and root.right is None:
    #         # this is faster and more clear than below
    #         return True if sum == 0 else False
    #     # if root.left is None and root.right is None and sum == 0:
    #     #     return True
    #     return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def hasPathSum(self, root, sum):
        stack = [(root, sum)]
        while stack:
            root, sum = stack.pop()
            if root:
                sum -= root.val
                if root.left is None and root.right is None and sum==0:
                    return True
                stack.append((root.right, sum))  # Note 似乎必须调换顺序. 
                stack.append((root.left, sum))
        return False
                

if __name__ == '__main__':
    """
    注意必须是root到leaf. 
    再写一个stack dfs
    """
    s = Solution()
        

