#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#
# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution(object):
    # def minDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     # This is the DFS version
    #     if not root:
    #         return 0
    #     left = self.minDepth(root.left)
    #     right = self.minDepth(root.right)
    #     if left == 0 or right == 0:
    #         return left + right + 1
    #     else:
    #         return min(left, right) + 1
    
    def minDepth(self, root):
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            size = len(queue)
            for _ in xrange(size):
                node = queue.popleft()  # Note this is not pop!!
                if node.left is None and node.right is None:
                    # Note this is a leaf!
                    return level + 1
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            level += 1

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

if __name__ == '__main__':
    """
    mini-depth的定义是从root到叶子节点的最短距离. leaf的定义是一个没有children的node. 
    BFS更快
    Note - can not directly use min(left, right) + 1 因为
        当root有一个分支是none的时候, depth不是1 ! 所以还需要额外的条件判断
    当只有一个root的时候, root本身也是一个leaf
    """
    s = Solution()
    tree = listToTree([3,9,20,None,None,15,7])
    tree = listToTree([1,2])
    tree = listToTree([1,2,3,4,None,None,5])
    print(s.minDepth(tree))
        

