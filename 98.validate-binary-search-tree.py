#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
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
    # pre = None  # Note这里赋值会导致测试失败. 因为有状态了! 需要重新创建Instance
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root:
    #         return True
    #     if not self.isValidBST(root.left):
    #         return False
    #     if self.pre and self.pre.val >= root.val:  # note >=
    #         return False
    #     self.pre = root
    #     if not self.isValidBST(root.right):
    #         return False
    #     return True

    def isValidBST(self, root):
        stack = []
        pre = None
        cur = root
        while cur or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pre is not None and pre >= cur.val:  # Note 这里不能if last!!!
                return False
            pre = cur.val
            cur = cur.right
        return True


if __name__ == '__main__':
    """
    我的思路:
    我一开始写得是preoder的错解, 思路是root的left right的值满足要求, 并且左右子树validate即可.
    但是这不能保证右子树所有的值都大于root. 要想preoder, 必须再传入当前的min和max...
    这道题必须要inorder!!! 所有与BST大小顺序相关的都要inorder. 
    答案思路: 
    解法1, preorder-recursion中记录之前的root(需要一个全局变量), 进行比较. 
    解法2, inorder iterative traversal: 
    TODO duplicate时怎么搞? 
    解法3, 当然也可以直接先traverse得到所有的值, 再循环一遍list...
    """
    s = Solution()
    print(s.isValidBST(listToTree([2,1,3])))
    s = Solution()
    print(s.isValidBST(listToTree([5,1,4,None,None,3,6])))
    s = Solution()
    print(s.isValidBST(listToTree([10,5,15,None,None,6,20])))    

