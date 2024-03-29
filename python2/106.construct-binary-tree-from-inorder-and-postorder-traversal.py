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
    #     if not inorder:  # 不能postorder
    #         return None 
    #     val = postorder.pop()
    #     root = TreeNode(val)
    #     idx = inorder.index(val)
    #     root.right = self.buildTree(inorder[idx + 1:], postorder)
    #     root.left = self.buildTree(inorder[:idx], postorder)
    #     return root

    def buildTree(self, inorder, postorder):
        def helper(lo, hi):  # [lo,hi)
            if lo < hi:
                val = postorder.pop()
                root = TreeNode(val)
                idx = inorder_dict[val]
                root.right = helper(idx + 1, hi)
                root.left = helper(lo, idx)
                return root
        inorder_dict = {n: i for i, n in enumerate(inorder)}
        lo, hi = 0, len(inorder)
        return helper(lo, hi)

if __name__ == '__main__':
    """
    解法1:
        中序遍历为：
            (中序遍历左分支) (根结点) (中序遍历右分支) 
        后序遍历为：
            (后序遍历左分支) (后序遍历右分支) (根结点)    
        通过中序遍历确定左右子树的分支. 
        post不需deque, 直接pop即可. 
    """
    s = Solution()
    print(treeToList(s.buildTree([9,3,15,20,7], [9,15,7,20,3])))

