#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
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
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     def helper(root, ans):
    #         if not root:
    #             return 
    #         helper(root.left, ans)
    #         ans.append(root.val)
    #         helper(root.right, ans)
    #     res = []
    #     helper(root, res)
    #     return res

    def inorderTraversal(self, root):
        sta = []
        ans = []
        # 可能出现sta为空但是root不空的情况，比如root的左边都结束
        while sta or root:  # sta里是左边的, root代表右边的root
            while root:  # 直到None的时候停下.  
                sta.append(root)
                root = root.left  
            cur = sta.pop()
            ans.append(cur.val)
            root = cur.right  # 可能是None
        return ans

if __name__ == '__main__':
    """
    解法1: 递归直接写掉.
    解法2:
        算法是对的, 没有证明? 没有完全理解. 
        先入栈所有左边的, 再逐个pop, 写值, 改root为right. 
        root代表的是新一个可能有left的地方
    解法3: 
        TODO 大雪菜还有个通用递归转换方法
        https://www.acwing.com/solution/LeetCode/content/176/
    解法4: Morris traversal: O(1)空间复杂度.. 很复杂. 不管 
    """
    s = Solution()
    print(s.inorderTraversal(listToTree([1,None,2,3])))
