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
    #     # 68.57%
    #     def helper(preorder, inorder):
    #         if inorder:  # 这里是inorder不是preorder...
    #             item = preorder.popleft()
    #             ind = inorder.index(item)
    #             node = TreeNode(item)
    #             node.left = helper(preorder, inorder[:ind])
    #             node.right = helper(preorder, inorder[ind + 1:])
    #             return node
    #     preorder = deque(preorder)
    #     return helper(preorder, inorder)

    def buildTree(self, preorder, inorder):
        # 99.83%
        def helper(low, high):  # [low, high)
            if low < high: 
                # item = preorder.popleft()
                item = next(pre_iter)
                ind = inorder_cache[item]
                node = TreeNode(item)
                node.left = helper(low, ind)
                node.right = helper(ind + 1, high)
                return node  # do not need to return None
        inorder_cache = {item: i for i, item in enumerate(inorder)}
        pre_iter = iter(preorder)
        # preorder = deque(preorder)
        return helper(0, len(inorder))

if __name__ == '__main__':
    """
    解法1: python答案里的图很棒
    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
    python答案太过简单. 这个preorder实际上也应该向inorder一样切分成两块. 
    但是因为传进去的是指针, 在第一个helper结束的时候preorder left的部分已经消失了, 
    所以可以有上述写法.
    如果不先转换成deque, 则需要每次pop(0), 还是比较慢.
    解法2:
        用iter(preorder)而不是转换成deque: 两种速度差不多
        inorder用dict记录位置: 但是不能在上面直接改... 因为每次输入inorder的slice改变了
        inorder的位置... 所以helper的输入必须改成当前inorder的start和end
    解法3:
        还有iterative的方案? 应该就不写了. 
    """
    s = Solution()
    print(treeToList(s.buildTree([3,9,20,15,7], [9,3,15,20,7])))

