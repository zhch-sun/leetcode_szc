#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None  # Note 必须有这里... 无法处理None input
        queue = deque([root])
        res = []
        level = 0
        while queue:
            size = len(queue)
            res_cur = [cur.val for cur in queue]
            if level % 2 == 1:
                res_cur.reverse()
            res.append(res_cur)
            for _ in range(size):
                cur = queue.popleft()
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
            level += 1
        return res
        
        
        
if __name__ == '__main__':
    """
    把res_cur部分放到下面的循环里, 可以实现insert(0)的做法. 但是我不喜欢.
    还是reverse吧. 
    """
    s = Solution()
    print(s.zigzagLevelOrder(listToTree([3,9,20,None,None,15,7])))
