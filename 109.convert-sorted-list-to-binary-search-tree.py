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
        def dfs(n):
            if n <= 0:  # 忘记了..
                return None  
            left = dfs(n / 2)
            tree = TreeNode(self.node.val)
            tree.left = left
            self.node = self.node.next
            tree.right = dfs(n - n / 2 - 1)
            return tree
        self.node = head  # 貌似只有builtin的[]和{}才能够在内部修改外部变量. node是不能直接修改的.
        count = 0
        cur = ListNode(None)
        cur.next = head
        while cur.next:
            count += 1
            cur = cur.next
        return dfs(count)

if __name__ == '__main__':
    """
    有一个做法是每次都用slow fast确定中点位置, 速度太慢了. nlog(n)
    答案的做法还是很高明的. 直接通过个数判断在数上的位置. 
    还有就是要把node写成self.node: 这是python作用域的问题了. 
    """
    s = Solution()

    print(treeToList(s.sortedListToBST(list2Node([-10,-3,0,5,9]))))

