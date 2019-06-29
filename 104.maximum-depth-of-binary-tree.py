#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

def listToTree(input):
    if not input:
        return None
    nodeQueue = [TreeNode(input[0])]
    index = 1
    front = 0
    while index < len(input):
        cur = nodeQueue[front]
        front += 1
        if input[index] is not None:
            cur.left = TreeNode(input[index])
            nodeQueue.append(cur.left)
        index += 1
        if index >= len(input):
            break

        if input[index] is not None:
            cur.right = TreeNode(input[index])
            nodeQueue.append(cur.right)
        index += 1
        nodeQueue.append(cur)
    return nodeQueue[0]

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
    TODO bfs solution
    """
    s = Solution()
    tree = listToTree([3,9,20,None,None,15,7])
    print(s.maxDepth(tree))
    # print(treeToList(tree))
