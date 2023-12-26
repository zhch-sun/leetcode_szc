#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(left, right):  # 必须要两个输入, 比较左右
            if left and right:
                return left.val == right.val and \
                    helper(left.left, right.right) and \
                    helper(left.right, right.left)
            else:
                return not left and not right  # 两个只有都是None才可以
        if not root:
            return True
        return helper(root.left, root.right)

    # def isSymmetric(self, root):
    #     if not root:
    #         return True
    #     sta = [root.left, root.right]
    #     while sta:
    #         right = sta.pop()
    #         left = sta.pop()
    #         if not left and not right:
    #             continue
    #         elif (not left or not right) or left.val != right.val:
    #             return False
    #         sta.append(left.left)
    #         sta.append(right.right)
    #         sta.append(left.right)
    #         sta.append(right.left)
    #     return True

if __name__ == '__main__':
    """
    注意理解题意. 还有 root=None的时候return True也是厉害. 
    要注意iterative时候的条件判断. 
    解法1: 递归
        根节点值相等, 左边左子树和右边右子树对称. 左边又子树, 右边左子树. 
        我一开始进行各种判断: 两个不存在True, 两个亦或False.
        答案的逻辑真巧妙... left is right厉害了...
    解法2: 迭代:
        实际上是level order! 层序遍历.
    解法3: 迭代, 未写
        可以按照中序遍历的考虑方式. 左边是左中右, 右边是右中左.
    """
    def T2L(n):
        # tree to list
        return T2L(n.left) + [n.val] + T2L(n.right) if n is not None else []
    s = Solution()

    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.right = TreeNode(3)
    # print(treeToList(tree))
    tree = listToTree([1,2,2,3,4,4,3])
    # tree = listToTree([1,2,2,None,3,None,3])
    # print(treeToList(tree))
    # print(tree)
    print(s.isSymmetric(tree))
