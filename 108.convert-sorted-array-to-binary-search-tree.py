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
    # def sortedArrayToBST(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: TreeNode
    #     """
    #     def convert(left, right):
    #         if left > right:
    #             return  # i forget that
    #         mid = left + (right - left) // 2
    #         cur = TreeNode(nums[mid])
    #         cur.left = convert(left, mid - 1)  # TODO 这里顺序和前面调换呢?
    #         cur.right = convert(mid + 1, right)
    #         return cur

    #     return convert(0, len(nums) - 1)

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        root = TreeNode(0)
        stack = [(root, 0, len(nums) - 1)]
        while stack:
            node, left, right = stack.pop()
            mid = left + (right - left) // 2
            node.val = nums[mid]

            if left <= mid - 1:
                node.left = TreeNode(0)
                # 函数的输入输出都应该压到栈里?
                stack.append([node.left, left, mid - 1])  # 每一个函数调用,压一次栈
            if mid + 1 <= right:
                node.right = TreeNode(0)
                stack.append((node.right, mid + 1, right))
        return root

if __name__ == '__main__':
    """
    TODO: 怎么证明是height-balance? 
    解法1:需要理解这个递归. 有点类似与二分查找. 
    解法2: 非iterative: 用一个栈模仿函数调用
    """
    s = Solution()
    print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))
