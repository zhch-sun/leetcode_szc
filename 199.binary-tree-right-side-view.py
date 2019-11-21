#
# @lc app=leetcode id=199 lang=python
#
# [199] Binary Tree Right Side View
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
    # def rightSideView(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """        
    #     if not root:
    #         return []
    #     dq = deque([root])
    #     ans = []
    #     while dq:
    #         ans.append(dq[-1].val)
    #         for _ in xrange(len(dq)):
    #             cur = dq.popleft()
    #             if cur.left:
    #                 dq.append(cur.left)
    #             if cur.right:
    #                 dq.append(cur.right)
    #     return ans    
        
    def rightSideView(self, root):
        def dfs(root, height):
            if root:
                if height >= len(ans):
                    ans.append(root.val)
                dfs(root.right, height + 1)
                dfs(root.left, height + 1)
        ans = []
        dfs(root, 0)
        return ans

if __name__ == '__main__':
    """
    解法1:
        迭代. level order traversal. 
        而且已经是最优, 因为必须traverse整个树才知道左边有没有更深的位置.
        既然遍历, 层序已经最优
    答案2: 
        递归. 需要当前的height
        preorder traversal: 顺序是root right left
        然而确实需要整个遍历一遍才能知道最终的答案. 
    """
    s = Solution()
    print(s.rightSideView(listToTree([1,2,3,None,5,None,4])))
