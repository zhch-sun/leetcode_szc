#
# @lc app=leetcode id=173 lang=python
#
# [173] Binary Search Tree Iterator
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

# class BSTIterator(object):
#     # 98%
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.stack = []
#         while root:
#             self.stack.append(root)
#             root = root.left

#     def next(self):
#         """
#         @return the next smallest number
#         :rtype: int
#         """
#         cur = self.stack.pop()
#         if cur.right:
#             item = cur.right
#             while item:
#                 self.stack.append(item)
#                 item = item.left
#         return cur.val

#     def hasNext(self):
#         """
#         @return whether we have a next smallest number
#         :rtype: bool
#         """
#         return len(self.stack) > 0

class BSTIterator(object):
    def __init__(self, root):
        self.sta = []
        self._addLeft(root)

    def next(self):
        cur = self.sta.pop()
        self._addLeft(cur.right)
        return cur.val      

    def hasNext(self):
        return len(self.sta) > 0

    def _addLeft(self, root):
        while root:
            self.sta.append(root)
            root = root.left

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    """
    解法1/ 解法2: 
        用stack, 迭代的中序遍历一个tree. 
        写的时候发现初始化和next函数可以共用代码, 所以抽象出一个函数. 
    """
    tree = listToTree([7,3,15,None,None,9,20])
    s = BSTIterator(tree)
    while s.hasNext():
        print(s.next())

