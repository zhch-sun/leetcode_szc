#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

def listToTree(input):
    if not input:
        return None
    root = TreeNode(int(input[0]))
    nodeQueue = [root]  # 最后这个包含所有node
    front = 0  # to index queue
    index = 1  # to index list
    while index < len(input):
        node = nodeQueue[front]
        front += 1

        left_num = input[index]
        if left_num is not None:
            # 这意味着前面的None会使后面的位置直接跳过
            node.left = TreeNode(left_num)
            nodeQueue.append(node.left)

        index += 1
        if index >= len(input):
            break

        right_num = input[index]
        if right_num is not None:
            node.right = TreeNode(right_num)
            nodeQueue.append(node.right)
        index += 1
    return root

def treeToList(input):
    if not input:
        return None
    cur = input
    nodeQueue = [cur]
    res = []
    front = 0
    while True:
        val = cur.val if cur is not None else None
        res.append(val)
        if cur is not None:  #及时该位置是空的，也要None?
            nodeQueue.append(cur.left)
            nodeQueue.append(cur.right)
        front += 1
        if front < len(nodeQueue):
            cur = nodeQueue[front]
        else:
            break
    while res[-1] is None:  # 符合定义?
        res.pop()
    return res

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    # def buildTree(self, preorder, inorder):
    #     """
    #     :type preorder: List[int]
    #     :type inorder: List[int]
    #     :rtype: TreeNode
    #     """        
    #     def helper(lo, hi):  # [lo, hi)
    #         if lo < hi:
    #             val = preorder.popleft()
    #             root = TreeNode(val)
    #             idx = inorder_dict[val]
    #             root.left = helper(lo, idx)
    #             root.right = helper(idx + 1, hi)
    #             return root
    #     preorder = deque(preorder)
    #     lo, hi = 0, len(inorder)
    #     inorder_dict = {n: i for i, n in enumerate(inorder)}
    #     return helper(lo, hi)

    def buildTree(self, preorder, inorder): 
        # 用iter减去O(N)的复杂度.     
        def helper(lo, hi):  # [lo, hi)
            if lo < hi:
                val = next(pre_iter)  # 不会stop iteration
                root = TreeNode(val)
                idx = inorder_dict[val]
                root.left = helper(lo, idx)
                root.right = helper(idx + 1, hi)
                return root
        pre_iter = iter(preorder)
        lo, hi = 0, len(inorder)
        inorder_dict = {n: i for i, n in enumerate(inorder)}
        return helper(lo, hi)

if __name__ == '__main__':
    """
    题设: 
        不存在重复元素, 重复元素好难? 
    解法1: 
        python答案里的图很棒
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
        python答案太过简单. 这个preorder实际上也应该向inorder一样切分成两块. 
        但是因为传进去的是指针, 在第一个helper结束的时候preorder left的部分已经消失了, 
        所以可以有上述写法.
        加速:
            preorder: 先转换成deque, 则可以用指针. 更快.
            inorder: 用dict记录位置
    解法2:
        preorder用指针, 理论更快
    解法3:
        iterative的方案不写.
    """
    s = Solution()
    print(treeToList(s.buildTree([3,9,20,15,7], [9,3,15,20,7])))

