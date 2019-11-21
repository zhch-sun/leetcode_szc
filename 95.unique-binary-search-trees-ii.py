#
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """        
        def dfs(lo, hi):  # [lo, hi] [1, N]
            if lo > hi:
                return [None]  # 要这么搞..
            if (lo, hi) in cache:
                return cache[lo, hi]
            cache[lo, hi] = []
            for i in xrange(lo, hi + 1):  # i就是元素名
                left = dfs(lo, i - 1)
                right = dfs(i + 1, hi)
                for l in left:  # 必须要三重循环..
                    for r in right:
                        root = TreeNode(i)  # 必须建立新node!
                        root.left = l
                        root.right = r
                        cache[lo, hi].append(root)
            return cache[lo, hi]
        if n == 0:
            return None
        cache = {} # 可以defaultdict
        dfs(1, n)
        return cache[1, n]

if __name__ == '__main__':
    """
    解法1: 
        记忆化搜索. 注意必须在 l和r的循环内部建立新root. 
        否则root的指向就不对了.
    解法2: LRU cache. 假设函数保证给定输入的情况下输出相同. 
        那么可以给函数加wrapper
        记录最近n个输入的函数的输出值. 如果再遇到相同输入直接从cache中读取. 
        cache是一个有序字典.
    """
    s = Solution()
    trees = s.generateTrees(3)
    for t in trees:
        print(treeToList(t))
        

