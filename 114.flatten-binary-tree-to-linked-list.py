#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
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
    # def flatten(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: None Do not return anything, modify root in-place instead.
    #     """
    #     def helper(root, pre):
    #         if root.right:
    #             pre = helper(root.right, pre)
    #         if root.left:
    #             pre = helper(root.left, pre)
    #         root.right = pre
    #         root.left = None
    #         return root
    #     if not root:
    #         return None
    #     return helper(root, None)

    def flatten(self, root):
        # corner case处理更优秀
        def helper(root, pre):
            if not root:
                return pre            
            pre = helper(root.right, pre)  # 还可以用全局变量传递pre,但是不推荐. 
            pre = helper(root.left, pre)
            root.right = pre
            root.left = None
            return root
        return helper(root, None)

    # def flatten2(self, root):
    #     # 还是preorder, 但是连在left上, 应该是正确的
    #     def helper(root, pre):
    #         if not root:
    #             return pre            
    #         pre = helper(root.right, pre)  # 还可以用全局变量传递pre,但是不推荐. 
    #         pre = helper(root.left, pre)
    #         root.left = pre
    #         root.right = None
    #         return root
    #     return helper(root, None)

if __name__ == '__main__':
    """
    理解题意: 输出的是个preorder的顺序, 连在right上. 
    https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share
    第一个java答案下面有图示过程.
    答案的过程和我想得是反的, 我希望把left插入到root和right之间, 而插入操作是难的.
    答案是把right接到左left的最后面. 大致思路是找到最right, 连到前一个left的flatten后的right上
    注意corner case的处理方法

    flatten2, 写了一个还是preorder的顺序, 但是连在left上的题. 
    因为我们要 上一个flatten连在新flatten后面!, 所以仍然需要先处理right再处理left
    """
    s = Solution()
    print(treeToList(s.flatten(listToTree([1,2,5,3,4,None,6]))))
