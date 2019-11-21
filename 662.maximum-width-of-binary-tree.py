#
# @lc app=leetcode id=662 lang=python
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dq = deque([(0, root)])
        ans = 0
        while dq:
            minV, maxV = float('inf'), float('-inf')  # Note 初始化啊...
            for _ in xrange(len(dq)):  # 不是只有边界上的才有用. 
                i, cur = dq.popleft()  # 顺序无关也必须popleft!
                minV = min(minV, i)
                maxV = max(maxV, i)
                if cur.left:
                    dq.append((i * 2, cur.left))
                if cur.right:
                    dq.append((i * 2 + 1, cur.right))
            ans = max(ans, maxV - minV + 1)
        return ans

if __name__ == '__main__':
    """
    定义是端点之间的长度.. 不能直接len(dq)
    """
    s = Solution()
# @lc code=end

