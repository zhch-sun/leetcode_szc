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
        def helper():
            if not nums:
                return None
            val = ''
            while nums and (nums[0].isdigit() or nums[0] == '-'):
                val += nums.popleft()
            node = TreeNode(int(val))  # 一定是一个值进入递归.
            if nums and nums[0] == '(':
                nums.popleft()  # pop '('
                node.left = helper()
                nums.popleft()  # pop ')'
            if nums and nums[0] == '(':
                nums.popleft()
                node.right = helper()
                nums.popleft()
            return node
        nums = deque(s)
        return helper()

if __name__ == '__main__':
    """
    还可以是负数, 由-号表示.. 
    值可能是42, -56, 872
    """
    s = Solution()
    print(s.str2tree("4(2(3)(1))(6(5))"))
    print(s.str2tree("4"))