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
    #     # left root right
    #     def helper(root, res):
    #         if root:
    #             helper(root.left, res)
    #             res.append(root.val)
    #             helper(root.right, res)
    #     res = []
    #     helper(root, res)
    #     return res
    
    def inorderTraversal(self, root):
        # 相对好理解. 如果当前node不为none, 就往left跑
        stack = []
        res = []
        cur = root
        while cur or stack: # 这个条件
            while cur is not None:  # 只有下面pop出值来才查左边?
                stack.append(cur)  #  这里add是current, 而不是left..
                cur = cur.left
            cur = stack.pop() # 注意这里必须pop, 因为上面的cur已经变成None..
            res.append(cur.val)  # cur has no left leaf
            cur = cur.right  # might be None
        return res

    # def inorderTraversal(self, root):
    #     # 合并了两个while循环. 这个最快... 
    #     stack = []
    #     res = []
    #     cur = root  # 可以直接用root. 
    #     while cur or stack: # 这个条件
    #         if cur is not None:  # 只有下面pop出值来才查左边?
    #             stack.append(cur)  #  这里add是current, 而不是left..
    #             cur = cur.left
    #         else:
    #             cur = stack.pop() # 注意这里必须pop, 因为上面的cur已经变成None..
    #             res.append(cur.val)  # cur has no left leaf
    #             cur = cur.right  # might be None
    #     return res

if __name__ == '__main__':
    """
    recursive很直接. 
    iterative: 
    解法1:
        就用这个解法. 
        push进去的是cur, 而不是current.left. 意思是push进去所有有left的node. 
        而不是push进去所有node的left children...
        TODO 这个题因为有两个不同位置的递归, 所以不能直接用stack做?
    解法2: 把两个while循环写到一起. 
    解法3: Morris traversal: O(1)空间复杂度.. 很复杂. 
    """
    s = Solution()
    print(s.inorderTraversal(listToTree([1,None,2,3])))
    
