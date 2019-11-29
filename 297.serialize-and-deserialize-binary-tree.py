#
# @lc app=leetcode id=297 lang=python
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return None
    #     nodeQueue = deque([root])
    #     res = []
    #     while nodeQueue:
    #         cur = nodeQueue.popleft()
    #         val = cur.val if cur else None
    #         res.append(val)
    #         if cur is not None:
    #             nodeQueue.append(cur.left)
    #             nodeQueue.append(cur.right)
    #     while res[-1] is None:  # 符合定义
    #         res.pop()
    #     return res

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """
    #     if not data:
    #         return None
    #     nums = data  # .split(',')
    #     N = len(nums)
    #     root = TreeNode(nums[0])
    #     dq = deque([root])  # 存储非None节点. 
    #     idx = 0  # 指向上一个位置.
    #     while True:  # 可能dq有值但是idx已经溢出. 因为叶子节点下面无None
    #         cur = dq.popleft()
            
    #         idx += 1  # 可以抽出一个函数. 
    #         if idx >= N:
    #             break
    #         left = nums[idx]
    #         if left is not None:  # 必须加is not None!
    #             cur.left = TreeNode(left)
    #             dq.append(cur.left)
            
    #         idx += 1
    #         if idx >= N:
    #             break
    #         right = nums[idx]
    #         if right is not None:
    #             cur.right = TreeNode(right)
    #             dq.append(cur.right)
    #     return root
    
    def serialize(self, root):
        def dfs(root):
            if root:
                ans.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                ans.append('#')
        ans = []  # 不能过滤最后的'#', 考虑到空输入...
        dfs(root)  # 不需要讨论空root
        return ','.join(ans)

    def deserialize(self, data):
        def dfs():  # 空输入
            if not nums:
                return None
            val = nums.popleft()  # 用iter也可, 但是要保证有足够的'#'在最后
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = dfs()
                node.right = dfs()
            return node

        nums = deque(data.split(','))  # 不是','.split(data)...
        return dfs()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

if __name__ == '__main__':
    """
    分析: 
        单纯遍历是不能还原, 但是多了None或者'#', 就可以. 
        我的方案就是一个前序遍历, 在需要的地方赋值'#'
    解法1:
        和leetcode的格式是一样的. level order traversal.
        就是一个deque
        方便起见没有转化成str. 
    解法2:
        preorder递归最简单.
        原答案还用了iter(), 假设字符串来自于serialize, 
        是刚好不会StopIteration的..
        还是deque好啊..
    submission中有更快的解法. 
    """
    codec = Codec()
    print(codec.serialize(codec.deserialize(','.join(map(str, [1,2,3,'#','#',4,5])))))
    # print(treeToList(listToTree([1,2,3,None,None,4,5])))