#
# @lc app=leetcode id=109 lang=python
#
# [109] Convert Sorted List to Binary Search Tree
#

def list2Node(input):
    dummy = ListNode(0)
    cur = dummy
    for item in input:
        cur.next = ListNode(item)
        cur = cur.next
    return dummy.next

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

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        next = ',' + self.next.__repr__() if self.next else ''
        return str(self.val) + next

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """        
        def dfs(cnt):
            if cnt == 0:  # 忘记了...
                return None 
            left = dfs(cnt // 2)
            cur = TreeNode(self.node.val)
            cur.left = left
            self.node = self.node.next  # 外层变量是不能直接赋值的
            cur.right = dfs(cnt - cnt // 2 - 1)
            return cur
        
        cur = head
        N = 0  # N 是数量.
        while cur:
            N += 1
            cur = cur.next
        self.node = head
        return dfs(N)


if __name__ == '__main__':
    """
    思路:
        重要的思路是inorder traversal!!! 因为inorder也是一个序列!!
    解法1:
        答案直接通过个数判断在树上的位置. (和108一样?)
        还有就是要把node写成self.node: 这是python作用域的问题了. 
    解法2:
        转成数组也可以....
    """
    s = Solution()

    print(treeToList(s.sortedListToBST(list2Node([-10,-3,0,5,9]))))

