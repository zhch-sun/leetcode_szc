#
# @lc app=leetcode id=107 lang=python
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def levelOrderBottom(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     if not root:
    #         return []
    #     res = deque()
    #     queue = deque([root])
    #     while queue:
    #         size = len(queue)
    #         level = []
    #         for _ in range(len(queue)):
    #             cur = queue.popleft()
    #             level.append(cur.val)
    #             if cur.left is not None:
    #                 queue.append(cur.left)
    #             if cur.right is not None:
    #                 queue.append(cur.right)
    #         res.appendleft(level)
    #     return list(res)
    def treeDepth(self, root):
        return 1 + max(self.treeDepth(root.left), self.treeDepth(root.right)) if root else 0

    def levelOrderBottom(self, root):
        if not root:
            return []
        # res = [[]] * self.treeDepth(root)  # Note same pointers!!!!
        res = [[] for _ in range(self.treeDepth(root))]
        queue = deque([root])
        height = 0
        while queue:
            size = len(queue)
            for _ in range(len(queue)):
                cur = queue.popleft()
                res[-(height + 1)].append(cur.val)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            height += 1
        return res
        
        
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

if __name__ == '__main__':
    """
    这个题应该就是102 + reverse了...
    不用reverse一个普遍的做法是在list最开始插入, 但这个操作是O(n)呀..
    注意如果用list的concat的化,也是O(n)的复杂度, 会生成一个新的list
    我的做法中bfs可以用deque实现. 但是最后还是要转成list, 这还是要O(n), 和reverse没啥区别..
    dfs似乎没有什么放啊. 
    """
    s = Solution()
    tree = listToTree([3,9,20,None,None,15,7])
    print(s.levelOrderBottom(tree))
    # print(treeToList(tree))
