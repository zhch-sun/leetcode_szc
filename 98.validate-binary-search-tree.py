#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
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
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """        
    #     def helper(root, lo, hi):  # 从上到下, 逐渐缩小合理范围. 
    #         if not root:
    #             return True
    #         if lo < root.val < hi:
    #             return helper(root.left, lo, root.val) and \
    #                 helper(root.right, root.val, hi)
    #         return False
    #     return helper(root, float('-inf'), float('inf'))

    def isValidBST(self, root):
        sta = []
        pre = float('-inf')
        while root or sta:
            while root:
                sta.append(root)
                root = root.left
            cur = sta.pop()
            if cur.val <= pre:  # 注意=号
                return False
            pre = cur.val
            root = cur.right  # 不是root.right...
        return True

if __name__ == '__main__':
    """
    题设: 判断是否为二叉搜索树. 
        每个节点大于所有左子树节点, 小于所有右子树节点. 算法书也是这么定义.
    解法1: 递归
        从下到上, 应该需要记录左子树的min和右子树的max? 
        从上到下, 逐步减小可行范围, 确保每个node都满足范围. 
    解法2: 
        迭代 中序遍历 inorder traversal
    """
    s = Solution()
    print(s.isValidBST(listToTree([2,1,3])))
    s = Solution()
    print(s.isValidBST(listToTree([5,1,4,None,None,3,6])))
    s = Solution()
    print(s.isValidBST(listToTree([10,5,15,None,None,6,20])))    

