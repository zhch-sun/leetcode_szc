#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """        
        if not root:
            return None
        ans = []
        dq = deque([root])
        level = 0  # 感觉level比一个flag还是要好
        while dq:
            if level & 1:  # deque的reverse没有copy!
                ans.append([x.val for x in reversed(dq)])
            else:  
                ans.append([x.val for x in dq])
            # if level & 1:  # 改良版 mod(2)
            #     ans[-1].reverse()
            for _ in xrange(len(dq)):
                cur = dq.popleft()
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            level += 1
        return ans

if __name__ == '__main__':
    """
    错解: 
        不能直接由popleft改为pop, 逻辑就错了.    
    解法1: reveres法
        1. 直接正常level, 把ans按照层数reverse...额外O(N)复杂度
        2. 给ans赋值时reverse dq, 这个复杂度是O(1)!
        3. 或者先计算dq长度, 然后赋值到最后.
    解法2:
        想要reverse dq里面的node, 失败了??!!
    解法3:
        双栈...不写
        s1 pushd到s2, s2 push到s1...
    """
    s = Solution()
    print(s.zigzagLevelOrder(listToTree([3,9,20,None,None,15,7])))
    print(s.zigzagLevelOrder(listToTree([1,2,3,4,None,None,5])))
