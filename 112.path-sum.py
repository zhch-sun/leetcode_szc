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
    # def hasPathSum(self, root, total):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: bool
    #     """        
    #     if not root:
    #         return False
    #     total -= root.val
    #     if not root.left and not root.right and total == 0:
    #         return True
    #     return self.hasPathSum(root.left, total) or \
    #         self.hasPathSum(root.right, total)

    def hasPathSum(self, root, total):
        # 这题允许sta中存None写法更简单.
        if not root:
            return False
        sta = [(root, total)]  # total表示没有算上root的total
        while sta:
            cur, total = sta.pop()
            total -= cur.val
            if not cur.left and not cur.right and total == 0:
                return True
            if cur.right:  # 忘记判断了..
                sta.append((cur.right, total))
            if cur.left:
                sta.append((cur.left, total))
        return False

if __name__ == '__main__':
    """
    题设: root2leaf. 存在负数.  
    解法1:
        正常的dfs
    解法2:
        迭代. preorder traversal
    """
    s = Solution()
        

