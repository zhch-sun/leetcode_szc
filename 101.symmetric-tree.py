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

class Solution(object):
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     def sym_helper(left, right):
    #         if left and right:
    #             return left.val == right.val and \
    #                 sym_helper(left.left, right.right) and \
    #                 sym_helper(left.right, right.left)
    #         else: # can be deleted
    #             return left is right
    #     if not root:
    #         return True  # None input return true
    #     # return not root or sym_helper(root.left, root.right)
    #     return sym_helper(root.left, root.right)

    def isSymmetric(self, root):
        if not root:
            return True
        stack = [root.left, root.right]
        while len(stack) > 0:
            left = stack.pop()
            right = stack.pop()
            if left is None and right is None:
                continue
            elif left is None or right is None or left.val != right.val: # Note this!
                return False
            stack.append(left.left)  # python do not have push
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True
        
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
    注意理解题意. 还有 root=None的时候return True也是厉害. 
    要注意iterative时候的条件判断. 
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
