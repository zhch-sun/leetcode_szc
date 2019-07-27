#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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

class Solution(object):
    # def buildTree(self, inorder, postorder):
    #     """
    #     :type inorder: List[int]
    #     :type postorder: List[int]
    #     :rtype: TreeNode
    #     """
    #     if inorder:
    #         item = postorder.pop()
    #         ind = inorder.index(item)
    #         node = TreeNode(item)
    #         node.right = self.buildTree(inorder[ind+1:], postorder)
    #         node.left = self.buildTree(inorder[0:ind], postorder)
    #         return node
        
    def buildTree(self, inorder, postorder):
        def helper(low, high):  # [low, high)
            if low < high:
                item = postorder.pop()
                ind = inorder_cache[item]
                node = TreeNode(item)
                node.right = helper(ind + 1, high)
                node.left = helper(low, ind)  # 这里写成(0,ind)了
                return node

        inorder_cache = {item: i for i, item in enumerate(inorder)}
        return helper(0, len(inorder))
if __name__ == '__main__':
    """
    在把上面的答案转换成下面的答案的时候, 遇到了若干问题..
    1. recurse出还是调用的self.buildTree... 实际上是helper
    2. helper的区间范围, 应该是(low, ind), 写成了(0,ind) 还是容易错呀..
    """
    s = Solution()
    print(treeToList(s.buildTree([9,3,15,20,7], [9,15,7,20,3])))

