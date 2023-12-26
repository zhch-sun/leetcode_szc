#
# @lc app=leetcode id=889 lang=python
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

from collections import deque
class Solution(object):
    # def constructFromPrePost(self, pre, post):
    #     """
    #     :type pre: List[int]
    #     :type post: List[int]
    #     :rtype: TreeNode
    #     """
    #     if not pre:
    #         return None
    #     root = TreeNode(pre.pop(0))
    #     if not pre:
    #         return root
    #     mid = post.index(pre[0]) + 1  # 当前先序左边的索引+1
    #     root.left = self.constructFromPrePost(\
    #         pre[:mid], post[:mid])  # 去掉第一个
    #     root.right = self.constructFromPrePost(\
    #         pre[mid:], post[mid:-1])  # 去掉最后一个
    #     return root

    def constructFromPrePost(self, pre, post):
        def dfs():
            root = TreeNode(pre[self.preIdx])
            self.preIdx += 1
            if root.val != post[self.posIdx]:
                root.left = dfs()
            if root.val != post[self.posIdx]:
                root.right = dfs()
            self.posIdx += 1  # 完成一个子树.
            return root
        self.preIdx = 0
        self.posIdx = 0
        return dfs()
        
if __name__ == '__main__':
    """
    分析:
        不唯一!
        前序和后序遍历, [1,2,3,None,5,6,7] 和 [1,2,3,5,None,6,7]是一样的..
        所以其实无法唯一确定子树顺序...
    解法1:
        前序遍历为：
            (根结点) (前序遍历左分支) (前序遍历右分支)
        后序遍历为：
            (后序遍历左分支) (后序遍历右分支) (根结点)
        如果知道preorder左分支的结点个数, 就能够判定树的形状.
        所以递归的时候不仅要处理root, 也要处理root后面的第一个元素
    解法2:
        用dict, deque, 输入a, b, c, d的解法错了...
        因为原来的算法是非常依赖相对位置的...
        而如果要用hash, 我只有绝对位置.. 坑爹啊...
    解法3:
        初始化preIdx=0和posIdx=0.
        按照pre_order的顺序.
        当root.val = post[posIdx]时, 搞定了子树. 
        如果不等, 则没有搞定子树. 
    """
    s = Solution()
    print(treeToList(s.constructFromPrePost(\
        [1,2,4,5,3,6,7], [4,5,2,6,7,3,1])))
    print(treeToList(s.constructFromPrePost(\
        [1,2,5,3,6,7], [5,2,6,7,3,1])))        
# @lc code=end
