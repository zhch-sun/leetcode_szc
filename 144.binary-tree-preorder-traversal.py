#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
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
    # def preorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """        
    #     def helper(root, ans):
    #         if not root:
    #             return
    #         ans.append(root.val)
    #         helper(root.left, ans)
    #         helper(root.right, ans)
    #     ans = []
    #     helper(root, ans)
    #     return ans

    # def preorderTraversal(self, root):
    #     # 这样判断条件更少. 而且速度更快. 
    #     sta = [root]  # 不需判断root非空
    #     ans = []
    #     while sta:
    #         cur = sta.pop()
    #         if cur:  # 还是直接把None都push进去
    #             ans.append(cur.val)
    #             sta.append(cur.right)  # 注意顺序! 先right在left
    #             sta.append(cur.left)
    #     return ans

    def preorderTraversal(self, root):
        # 这种是标准写法. 
        if not root:
            return []
        sta = [root]  # 不需判断root非空
        ans = []
        while sta:
            cur = sta.pop()
            ans.append(cur.val)
            if cur.right:
                sta.append(cur.right)
            if cur.left:
                sta.append(cur.left)
        return ans

if __name__ == '__main__':
    """
    解法1: 递归简单
    解法2: 迭代
        None也push进去. 这样代码更简单. 速度更快
    解法3:
        标准迭代写法. stack中一定是有意义的元素. 
        写这种.
    """
    s = Solution()
    # print(s.preorderTraversal(listToTree([1,None,2,3])))
    print(s.preorderTraversal(listToTree([1,2,3,None,5,6,7])))
    print(s.preorderTraversal(listToTree([1,2,3,5,None,6,7])))
    
