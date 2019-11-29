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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """        
        if not inorder:  # Note 不能是preorder!
            return None
        val = preorder.pop(0)  # 直接
        root = TreeNode(val)
        idx = inorder.index(val)
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root
    
    # def buildTree(self, preorder, inorder):
    #     # 错解: 仍然copy inorder但是用hash
    #     # .

    # def buildTree(self, preorder, inorder):
    #     def dfs(lo, hi):  # [lo, hi)
    #         if lo < hi:
    #             val = preorder.popleft()
    #             root = TreeNode(val)
    #             idx = inorder_dict[val]
    #             root.left = dfs(lo, idx)
    #             root.right = dfs(idx + 1, hi)
    #             return root
    #     preorder = deque(preorder)  # 或者用iter()
    #     lo, hi = 0, len(inorder)
    #     inorder_dict = {n: i for i, n in enumerate(inorder)}
    #     return dfs(lo, hi)

if __name__ == '__main__':
    """
    题设: 
        不存在重复元素
    解法1: 
        前序遍历为：
            (根结点) (前序遍历左分支) (前序遍历右分支)
        中序遍历为：
            (中序遍历左分支) (根结点) (中序遍历右分支) 
        通过inorder判断左右子树, 而且不能确定preorder的范围. 
        只能一个一个pop preorder里的元素. 
    解法2: 
        错解: 
            仍然copy array, 但是用dict. 
            此时inorder传进去的位置已经变了, hash内指向错误的位置..
        正解:
            preorder: 先转换成deque, 或用iter(). 更快.
            inorder: 用dict记录位置, 必须同时传进去(lo, hi)
    解法3:
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34543/Simple-O(n)-without-map
        把两个输入都reverse, 不需要deque和dict. 
        不写. 
    解法4:
        iterative的方案不写.
    """
    s = Solution()
    print(treeToList(s.buildTree([3,9,20,15,7], [9,3,15,20,7])))

