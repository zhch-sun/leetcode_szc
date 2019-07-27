#
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
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
#     def generateTrees(self, n):
#         """
#         :type n: int
#         :rtype: List[TreeNode]
#         """
#         # 87%
#         def helper(low, high):
#             # low high 都能被取到
#             if high < low: # 等于的时候也需要return
#                 return [None]  # 注意必须是None, 因为还要连在left和right上
#             trees = []
#             for i in range(low, high + 1):
#                 left = helper(low, i - 1)
#                 right = helper(i + 1, high)
#                 for l in left:
#                     for r in right:
#                         node = TreeNode(i)
#                         node.left = l
#                         node.right = r
#                         trees.append(node)
#             return trees
        
#         return helper(1, n) if n > 0 else []

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 98%
        cache = {}
        def helper(low, high):
            # low high 都能被取到
            if high < low: # 等于的时候也需要return
                return [None]  # 注意必须是None, 因为还要连在left和right上
            if (low, high) in cache:
                return cache[(low, high)]
            trees = []
            for i in range(low, high + 1):
                left = helper(low, i - 1)
                right = helper(i + 1, high)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        trees.append(node)
            cache[(low, high)] = trees
            return trees
        
        return helper(1, n) if n > 0 else []

if __name__ == '__main__':
    """
    解法1: 就是穷举. 注意必须是i-1 i+1, 我一开始放的i...
    因为recursion, 树是从下向上生长的. 注意返回的list of trees
    corner case: 答案里有更短的处理方案, 利用and. 但是影响可读性. 

    解法2: 加速方案: 可以添加一个cache, 存着从low~high的结果. python3可以直接用lru_cache. 
    python2要手写. 注意cache相当于全局变量. 但是有了cache之后相当于多个tree会共用一个subtree?

    TODO LRU cache
    """
    s = Solution()
    trees = s.generateTrees(3)
    for t in trees:
        print(treeToList(t))
        

