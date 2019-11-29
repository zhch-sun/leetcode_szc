# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        def dfs():
            if not nums:
                return None
            val = ''
            while nums and (nums[0].isdigit() or nums[0] == '-'):
                val += nums.popleft()
            node = TreeNode(int(val))  # 一定是一个值进入递归.
            if nums and nums[0] == '(':
                nums.popleft()  # pop '('
                node.left = dfs()
                nums.popleft()  # pop ')'
            if nums and nums[0] == '(':
                nums.popleft()
                node.right = dfs()
                nums.popleft()
            return node
        nums = deque(s)
        return dfs()

if __name__ == '__main__':
    """
    题设:
        从一个包括括号和整数的字符串构建一棵二叉树, 
        root后面可能有0,1,2对括号. "4(2(3)(1))(6(5))"
        里面可能与负数. 比如 '-42'
    解法:
        模拟.
    """
    s = Solution()
    print(s.str2tree("4(2(3)(1))(6(5))"))
    print(s.str2tree("4"))