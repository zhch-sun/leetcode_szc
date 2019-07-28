#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
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
    # def sumNumbers(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     def dfs(root, path_sum, total):
    #         path_sum = path_sum * 10 + root.val
    #         if (not root.left) and (not root.right):  # left
    #             return total + path_sum
    #         if root.left:
    #             total = dfs(root.left, path_sum, total)
    #         if root.right:
    #             total = dfs(root.right, path_sum, total)
    #         return total
    #     if not root:
    #         return 0            
    #     return dfs(root, 0, 0)
    
    # def sumNumbers(self, root):
    #     def dfs(root, path_sum):
    #         if not root:
    #             return 0     
    #         path_sum = path_sum * 10 + root.val
    #         if (not root.left) and (not root.right):  # left
    #             return path_sum
    #         return dfs(root.left, path_sum) + dfs(root.right, path_sum)
    #     return dfs(root, 0)   

    def sumNumbers(self, root):
        stack = [(root, 0)]
        res = 0
        while stack:
            root, path_sum = stack.pop()
            if root:
                path_sum = path_sum * 10 + root.val
                if (not root.left) and (not root.right):
                    res += path_sum
                stack.append((root.right, path_sum))
                stack.append((root.left, path_sum))      
        return res         


if __name__ == '__main__':
    """
    有关root = None的判断: 还是允许None为root, 在函数执行的前面处理比较好. 在递归调用时
        做判断感觉还是不方便.
    解法1: 两个输入: path_sum 和total
    解法2: 更好的解法. 
        一个输入path_sum, return的是以当前root为开始的total.
    解法3: dfs + stack
    解法4: bfs + queue: 没必要, 不写. 
    """
    s = Solution()
    print(s.sumNumbers(listToTree([4,9,0,5,1])))
