11#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def helper(root, sum, tmp, res):
            sum -= root.val
            tmp.append(root.val)
            if root.left is None and root.right is None:
                if sum == 0:
                    res.append(tmp[:])
                tmp.pop()  #所有return前都要pop()
                return
            if root.left:
                helper(root.left, sum, tmp, res)
            if root.right:
                helper(root.right, sum, tmp, res)
            tmp.pop()
        
        if not root:
            return []
        res = []
        helper(root, sum, [], res)
        return res
        
if __name__ == '__main__':
    """
    和前面的区别是前面只要返回是否存在,
    解法1:
        这题返回所有解. backtracking可以.
    解法2: 更短
        不用backtracking, 每次都返回一个新的list: 但这个需要每次都copy了.
        解法2不写了. 
    """
    s = Solution()
    print(s.pathSum(listToTree([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22))
