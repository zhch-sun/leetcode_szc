#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """        
        def dfs(lo, hi):  # [lo, hi]
            if lo > hi:
                return None
            mid = lo + (hi - lo) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(lo, mid - 1)
            root.right = dfs(mid + 1, hi)
            return root
        N = len(nums)
        return dfs(0, N - 1)

    # def sortedArrayToBST(self, nums):
    #     if not nums:
    #         return None
    #     root = TreeNode(0)
    #     stack = [(root, 0, len(nums) - 1)]
    #     while stack:
    #         node, left, right = stack.pop()
    #         mid = left + (right - left) // 2
    #         node.val = nums[mid]

    #         if left <= mid - 1:
    #             node.left = TreeNode(0)
    #             # 函数的输入输出都应该压到栈里?
    #             stack.append([node.left, left, mid - 1])  # 每一个函数调用,压一次栈
    #         if mid + 1 <= right:
    #             node.right = TreeNode(0)
    #             stack.append((node.right, mid + 1, right))
    #     return root

if __name__ == '__main__':
    """
    解法1: 
        二分, 个数是平衡的. 但是怎么证明呢?
    解法2: 
        迭代: 用一个栈模仿函数调用
    """
    s = Solution()
    print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
